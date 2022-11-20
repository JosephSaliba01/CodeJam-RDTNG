from model import QModel
from transformers import T5Tokenizer, logging


class QuestionGeneration:

    def __init__(self):
        logging.set_verbosity_error()
        self.model = QModel().load_from_checkpoint("checkpoints/best-checkpoint.ckpt")
        self.model.freeze()
        self.tokenizer = T5Tokenizer.from_pretrained("t5-base")
        self.tokenizer.add_special_tokens(
            {"additional_special_tokens": ["<hl>", "</hl>", "<sep>"]})

    def generateQA(self, input_str: str):

        # Clean the input string
        input_str = input_str.replace("\n", " ").replace("\t", " ").replace("extract answer:", "").replace(
            "extract question:", "").replace("<hl>", "").replace("</hl>", "").replace("<sep>", "").replace("</s>", "").strip()

        answer_extraction_encoding = self.tokenizer(
            f"extract answer: <hl> {input_str} </hl>",
            max_length=400,
            padding="max_length",
            truncation=True,
            return_attention_mask=True,
            add_special_tokens=True,
            return_tensors="pt"
        )

        answer_generated_ids = self.model.model.generate(
            input_ids=answer_extraction_encoding["input_ids"],
            attention_mask=answer_extraction_encoding["attention_mask"],
            max_length=50,
            num_beams=2,
            repetition_penalty=2.5,
            early_stopping=True,
            use_cache=True
        )

        answer_preds = [
            self.tokenizer.decode(
                gen_id, skip_special_tokens=False, clean_up_tokenization_spaces=True)
            for gen_id in answer_generated_ids
        ]

        outputList = []
        question_query = input_str

        answers = ("".join(answer_preds)).replace(
            "</s>", "").replace("<pad>", "").split("<sep>")
        for answer in answers:
            answer = answer.strip()
            if (answer != ""):
                outputList.append({"answer": answer})
                question_query = question_query.replace(
                    answer, f"<hl> {answer} </hl>", 1)

        question_extraction_encoding = self.tokenizer(
            f"extract question: {question_query}",
            max_length=400,
            padding="max_length",
            truncation=True,
            return_attention_mask=True,
            add_special_tokens=True,
            return_tensors="pt"
        )

        question_generated_ids = self.model.model.generate(
            input_ids=question_extraction_encoding["input_ids"],
            attention_mask=question_extraction_encoding["attention_mask"],
            max_length=100,
            num_beams=2,
            repetition_penalty=2.5,
            early_stopping=True,
            use_cache=True
        )

        question_preds = [
            self.tokenizer.decode(
                gen_id, skip_special_tokens=False, clean_up_tokenization_spaces=True)
            for gen_id in question_generated_ids
        ]

        questions = ("".join(question_preds)).replace(
            "</s>", "").replace("<pad>", "").split("<sep>")
        for i in range(len(questions)):
            questions[i] = questions[i].strip()
            if (questions[i] != "" and questions[i][-1] == "?"):
                outputList[i]["question"] = questions[i]

        return outputList

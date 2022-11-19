from model import QModel
from transformers import T5Tokenizer, logging

def test(input_text):
    # Silent the warnings
    logging.set_verbosity_error()
    model = QModel().load_from_checkpoint("checkpoints/best-checkpoint.ckpt")
    model.freeze()

    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    tokenizer.add_special_tokens({"additional_special_tokens": ["<hl>", "</hl>", "<sep>"]})

    answer_extraction_encoding = tokenizer(
        f"extract answer: <hl> {input_text} </hl>",
        max_length=400,
        padding="max_length",
        truncation=True,
        return_attention_mask=True,
        add_special_tokens=True,
        return_tensors="pt"
    )

    answer_generated_ids = model.model.generate(
        input_ids=answer_extraction_encoding["input_ids"],
        attention_mask=answer_extraction_encoding["attention_mask"],
        max_length=50,
        num_beams=2,
        repetition_penalty=2.5,
        early_stopping=True,
        use_cache=True
    )

    answer_preds = [
        tokenizer.decode(gen_id, skip_special_tokens=False, clean_up_tokenization_spaces=True)
        for gen_id in answer_generated_ids
    ]

    
    question_query = input_text

    answers = ("".join(answer_preds)).replace("</s>", "").replace("<pad>", "").split("<sep>")
    for answer in answers:
        if (answer.strip() != ""):
            answer = answer.strip()
            print(answer)
            question_query = question_query.replace(answer, f"<hl> {answer} </hl>", 1)

    question_extraction_encoding = tokenizer(
        f"extract question: {question_query}",
         max_length=400,
        padding="max_length",
        truncation=True,
        return_attention_mask=True,
        add_special_tokens=True,
        return_tensors="pt"
    )

    question_generated_ids = model.model.generate(
        input_ids=question_extraction_encoding["input_ids"],
        attention_mask=question_extraction_encoding["attention_mask"],
        max_length=50,
        num_beams=2,
        repetition_penalty=2.5,
        early_stopping=True,
        use_cache=True
    )

    question_preds = [
        tokenizer.decode(gen_id, skip_special_tokens=False, clean_up_tokenization_spaces=True)
        for gen_id in question_generated_ids
    ]

    print(question_preds)



if __name__ == "__main__":
    test("The Enumclaw horse sex case was a series of incidents in 2005 involving Kenneth Pinyan, an engineer who worked for Boeing and resided in Gig Harbor, Washington; James Michael Tait, a truck driver; and other unidentified men. Pinyan and Tait filmed and distributed zoophilic pornography of Pinyan receiving anal sex from a stallion under the alias 'Mr. Hands'. After engaging in this activity on multiple occasions over an unknown span of time, Pinyan received fatal internal injuries in one such incident. The story was reported in The Seattle Times and was one of that paper's most read stories of 2005. Pinyan's death rapidly prompted the enactment of a bill by the Washington State Legislature that prohibits both sex with animals and the videotaping of such an act. Under current Washington law, bestiality is now a Class C felony punishable by up to five years in prison")
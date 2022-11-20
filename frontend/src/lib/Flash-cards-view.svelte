<script>
  import Cards from './Cards.svelte';
  import { appState, currentNote } from '../store.js';
  import { jsPDF } from 'jspdf';
  import { element } from 'svelte/internal';

  let showEditor = () => appState.set('editor');
  let generatePdf = () => {
    const pdf = new jsPDF();

    pdf.text('Questions', 10, 10);
    $currentNote.questions.forEach((element, index) => {
      pdf.text(index + 1 + '.' + ' ' + element.query, 10, (index + 2) * 10);
    });
    pdf.text('Answers', 10, ($currentNote.questions.length + 2) * 10);

    $currentNote.questions.forEach((element, index) => {
      pdf.text(
        index + 1 + '.' + ' ' + element.answer,
        10,
        ($currentNote.questions.length + 3 + index) * 10
      );
    });

    pdf.save('quiz.pdf');
  };
</script>

<button on:click={showEditor}>Back to editor</button>
<button on:click={generatePdf}>Generate PDF</button>
<Cards/>

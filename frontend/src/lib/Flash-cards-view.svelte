<script>
  import Cards from './Cards.svelte';
  import { appState, currentNote } from '../store.js';
  import { jsPDF } from 'jspdf';
  import { element } from 'svelte/internal';

  let showEditor = () => appState.set('editor');
  let generatePdf = () => {
    const pdf = new jsPDF();
    pdf.setFontSize(8);

    pdf.text('Questions', 10, 10);
    $currentNote.questions.forEach((element, index) => {
      pdf.text(index + 1 + '.' + ' ' + element.query, 10, 10 + (index + 1) * 5);
    });

    pdf.addPage();
    pdf.text('Answers', 10, 10);

    $currentNote.questions.forEach((element, index) => {
      pdf.text(
        index + 1 + '.' + ' ' + element.answer,
        10,
        10 + (index + 1) * 5
      );
    });

    pdf.save('quiz.pdf');
  };
</script>

<button on:click={showEditor}>Back to editor</button>
<button on:click={generatePdf}>Generate PDF</button>
<Cards />

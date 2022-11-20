<script>
  import Cards from './Cards.svelte';
  import { appState, currentNote } from '../store.js';
  import { jsPDF } from 'jspdf';
  import { element } from 'svelte/internal';

  let showEditor = () => appState.set('editor');
  let generatePdf = () => {
    const pdf = new jsPDF();

    pdf.setFontSize(16);
    pdf.text('Questions', 10, 10);

    pdf.setFontSize(10);
    $currentNote.questions.forEach((element, index) => {
      let value = index % 25;
      if (index != 0 && value == 0) pdf.addPage();
      pdf.text(index + 1 + '.' + ' ' + element.query, 10, (value + 2) * 10);
    });

    pdf.addPage();
    pdf.setFontSize(16);
    pdf.text('Answers', 10, 10);
    pdf.setFontSize(10);
    $currentNote.questions.forEach((element, index) => {
      let value = index % 25;
      if (index != 0 && value == 0) pdf.addPage();
      pdf.text(index + 1 + '.' + ' ' + element.answer, 10, (value + 2) * 10);
    });

    pdf.save('quiz.pdf');
  };
</script>

<button on:click={showEditor}>Back to editor</button>
<button on:click={generatePdf}>Generate PDF</button>
<Cards />

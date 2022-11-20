<script>
  import { onDestroy } from 'svelte';
  import { loop_guard } from 'svelte/internal';
  import { currentNote, current_Q_index } from '../store.js';
  import QuizCard from './QuizCard.svelte';

  let questions = null;

  const unsubscribeToCurrentNote = currentNote.subscribe((value) => {
    if (value != null) questions = value.questions;
  });

  onDestroy(() => unsubscribeToCurrentNote());

  function nextCard() {
    if ($current_Q_index < questions.length - 1) {
      current_Q_index.set($current_Q_index + 1);
    }
  }

  function prevCard() {
    if ($current_Q_index > 0) {
      current_Q_index.set($current_Q_index - 1);
    }
  }

</script>

{#if Array.isArray(questions)}
  {#if questions.length > $current_Q_index}
    <QuizCard
      query={questions[$current_Q_index].query}
      choices={questions[$current_Q_index].choices}
      answer={questions[$current_Q_index].answer}
    />
    <div class="cards-view-bottom">
      <button on:click={prevCard}>&#60</button>
        {$current_Q_index + 1} / {questions.length}
      <button on:click={nextCard}>&#62</button>
    </div>  
  {/if}
{/if}



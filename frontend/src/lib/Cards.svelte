<script>
  import { onDestroy } from 'svelte';
  import { currentNote, current_FC_index} from '../store.js';
  import Card from './Card.svelte';

  let questions = null;

  const unsubscribeToCurrentNote = currentNote.subscribe((value) => {
    if (value != null) questions = value.questions;
  });

  function nextCard() {
    if ($current_FC_index < questions.length - 1) {
      current_FC_index.set($current_FC_index + 1);
    }
  }

  function prevCard() {
    if ($current_FC_index > 0) {
      current_FC_index.set($current_FC_index - 1);
    }
  }

  onDestroy(() => unsubscribeToCurrentNote());
</script>

{#if Array.isArray(questions)}
  {#if questions.length > $current_FC_index}
  <Card query={questions[$current_FC_index].query} answer={questions[$current_FC_index].answer} />
  <div class="cards-view-bottom" >
    <button on:click={prevCard}>&#60</button>
    {$current_FC_index + 1} / {questions.length}
    <button on:click={nextCard}>&#62</button>
  </div>
  {/if}
{/if}

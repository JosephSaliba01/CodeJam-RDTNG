<script>
  import { onDestroy } from 'svelte';
  import { currentNote } from '../store.js';
  import Card from './Card.svelte';

  let questions = null;

  const unsubscribeToCurrentNote = currentNote.subscribe((value) => {
    if (value != null) questions = value.questions;
  });

  onDestroy(() => unsubscribeToCurrentNote());
</script>

{#if Array.isArray(questions)}
  {#each questions as question}
    <Card query={question.query} answer={question.answer} />
  {/each}
{/if}

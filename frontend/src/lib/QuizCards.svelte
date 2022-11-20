<script>
    import { onDestroy } from 'svelte';
    import { loop_guard } from 'svelte/internal';
    import { currentNote } from '../store.js';
    import QuizCard from './QuizCard.svelte';
  
    let questions = null;
  
    const unsubscribeToCurrentNote = currentNote.subscribe((value) => {
      if (value != null) questions = value.questions;
    });
  
    onDestroy(() => unsubscribeToCurrentNote());
</script>
  
  {#if Array.isArray(questions)}
    {#each questions as question}
      console.log(question)
      <QuizCard query={question.query} choices={question.choices} />
    {/each}
  {/if}
  
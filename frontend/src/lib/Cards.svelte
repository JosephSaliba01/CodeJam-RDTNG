<script>
  import { questions } from '../store.js';
</script>

{#if Array.isArray($questions)}
  {#each $questions as question}
    <p>{question.answer}</p>
    <p>{question.query}</p>
  {/each}
{/if}

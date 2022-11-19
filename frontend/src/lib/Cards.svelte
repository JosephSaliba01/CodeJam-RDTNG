<script>
  import { questions } from '../store.js';
</script>

{#if Array.isArray($questions)}
  {#each $questions as question}
    <div class="card">
      <p>{question.answer}</p>
      <p>{question.query}</p>
      <p>fsdgds</p>
    </div>
  {/each}
{/if}

<style>
  .card {
    background-color: black;
  }
</style>

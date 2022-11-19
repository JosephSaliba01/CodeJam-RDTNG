<script>
  export let query;
  export let answer;

  let showAnswer = false;
</script>

<div class="question-div">
  {#if showAnswer}
    <p id="answer">{answer}</p>
  {:else}
    <p id="query">{query}</p>
  {/if}
</div>

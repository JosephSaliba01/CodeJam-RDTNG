<script>
  export let query;
  export let answer;

  let showAnswer = false;

  let toggleAnswer = () => {
    showAnswer = !showAnswer;
  };
</script>

<div class="question-div" on:click={toggleAnswer}>
  {#if showAnswer}
    <p id="answer">{answer}</p>
  {:else}
    <p id="query">{query}</p>
  {/if}
</div>

<style>
  .question-div {
    margin: 10%;
    background-color: white;
    border-radius: 5px;
  }
</style>

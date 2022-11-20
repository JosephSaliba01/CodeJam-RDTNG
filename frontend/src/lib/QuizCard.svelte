<script>
  export let query;
  export let choices;
  export let answer;
</script>

<div id="quiz-card-main-view">
  <div id="quiz-card-question-view">
    <p>{query}</p>
  </div>
  <div id="quiz-card-choices-view">
    {#if Array.isArray(choices)}
      {#each choices as choice}
        <button class="quiz-card-choice-button">{choice}</button>
      {/each}
    {/if}
  </div>
</div>

<style>
  .quiz-card-main-view {
    background-color: white;
    height: 12vh;
    width: 15vw;
    margin: 10%;
    border-radius: 5px;
    display: grid;
    grid-template-columns: 1fr;
  }

  .question-div div {
    grid-row-start: 1;
    grid-column-start: 1;
  }
</style>

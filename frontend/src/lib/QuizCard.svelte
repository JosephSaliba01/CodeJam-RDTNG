<script>
  export let query;
  export let choices;
  export let answer;

  let answered = false;
  let correct = false;

  let checkAnswer = (choice) => {
    console.log('hi');
    if (choice === answer) {
      correct = true;
    }
    answered = true;
  };
</script>

<div
  id="quiz-card-main-view"
  class={correct ? 'correct' : 'wrong'}
  class:answered
>
  <div id="quiz-card-question-view" class="p-container">
    <p>{query}</p>
  </div>
  <div
    id="quiz-card-answer-view"
    class="{answered ? '' : 'hidden'} p-container"
  >
    <p>{answer}</p>
  </div>
  <div id="quiz-card-choices-view">
    {#if Array.isArray(choices)}
      {#each choices as choice, i}
        <button
          class="quiz-card-choice-button color{i}"
          on:click={() => checkAnswer(choice)}
          disabled={answered}
          >{choice}
        </button>
      {/each}
    {/if}
  </div>
</div>

<style>
  p {
    margin-bottom: 0;
  }

  .hidden {
    visibility: hidden;
  }

  .answered.correct {
    background-color: rgb(154, 255, 154) !important;
    transition: 0.1s ease-out;
  }

  .answered.wrong {
    background-color: rgb(255, 140, 140) !important;
    transition: 0.1s ease-out;
  }

  #quiz-card-main-view {
    background-color: white;
    height: 30vh;
    width: 30vw;
    margin: 10% 0;
    border-radius: 10px;
    display: grid;
  }

  #quiz-card-choices-view {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
  }

  button {
    border-radius: 0;
  }

  .color0 {
    background-color: rgb(161, 241, 241);
    border-top-left-radius: 10px;
  }
  .color1 {
    background-color: rgb(255, 253, 185);
    border-top-right-radius: 10px;
  }
  .color2 {
    background-color: rgb(176, 156, 249);
    border-bottom-left-radius: 10px;
  }
  .color3 {
    background-color: rgb(255, 172, 244);
    border-bottom-right-radius: 10px;
  }
</style>

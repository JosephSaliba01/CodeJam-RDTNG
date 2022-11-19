<script>
  export let query;
  export let answer;
  import { flip } from 'svelte/animate';

  let showAnswer = false;

  let toggleAnswer = () => {
    showAnswer = !showAnswer;
  };
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="question-div" on:click={toggleAnswer}>
  <div class={showAnswer ? 'shown' : 'hidden'}><p id="answer">{answer}</p></div>
  <div class={showAnswer ? 'hidden' : 'shown'}><p id="query">{query}</p></div>
</div>

<style>
  .question-div {
    background-color: white;
    height: 12vh;
    width: 15vw;
    margin: 10%;
    border-radius: 5px;
    display: grid;
    grid-template-columns: 1fr;
  }

  .shown {
    opacity: 1;
    transition: opacity 0.2s linear;
  }

  .hidden {
    visibility: hidden;
    opacity: 0;
    transition: visibility 0s 0.2s, opacity 0.2s linear;
  }

  .question-div div {
    grid-row-start: 1;
    grid-column-start: 1;
  }
</style>

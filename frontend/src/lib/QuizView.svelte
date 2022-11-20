<script>
  import QuizCards from './QuizCards.svelte';
  import { appState } from '../store';
  let showEditor = () => appState.set('editor');

</script>

<div>
  <button on:click={showEditor}>End quiz</button>
</div>


<QuizCards />

<style>
  main {
    width: 600px;
    margin: 0 auto;
  }

  button {
    min-height: 3rem;
    padding-left: 1rem;
    padding-right: 1rem;
    margin-bottom: 1rem;
  }
</style>

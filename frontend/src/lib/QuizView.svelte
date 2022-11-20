<script>
  import QuizCards from './QuizCards.svelte';
  import { appState } from '../store';
  let showEditor = () => appState.set('editor');
</script>

<button on:click={showEditor}>End quiz</button>

<QuizCards />

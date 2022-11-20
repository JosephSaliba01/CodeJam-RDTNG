<script>
  import QuizCards from './QuizCards.svelte';
  import { appState } from '../store';
  let showEditor = () => appState.set('editor');
</script>

<div>
  <button on:click={showEditor}>End quiz</button>
</div>
<QuizCards />

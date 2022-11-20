<script>
    import QuizCards from "./QuizCards.svelte";
    let showEditor = () => appState.set('editor');
</script>
  <button on:click={showEditor}>End quiz</button>

<QuizCards/>
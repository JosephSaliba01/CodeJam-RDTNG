<script>
  import Cards from './Cards.svelte';
  import { appState } from '../store.js';

  let showEditor = () => appState.set('editor');
</script>

<button on:click={showEditor}>Back to editor</button>
<Cards />

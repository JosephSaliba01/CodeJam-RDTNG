<script>
  import Editor from './lib/Editor.svelte';
  import FlashCardsView from './lib/Flash-cards-view.svelte';
  import Quiz from './lib/Quiz.svelte';
  import QuizView from './lib/QuizView.svelte';
  import { appState } from './store.js';
  console.log($appState === 'editor');
</script>

<main>
  <div class={$appState === 'editor' ? '' : 'hidden'}>
    <Editor />
  </div>
  <div class={$appState === 'flashCards' ? '' : 'hidden'}>
    <FlashCardsView />
  </div>
  <div class={$appState === 'quiz' ? '' : 'hidden'}>
    <QuizView/>
  </div>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
  .hidden {
    display: none;
  }
</style>

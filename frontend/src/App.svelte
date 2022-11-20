<script>
  import Editor from './lib/Editor.svelte';
  import FlashCardsView from './lib/Flash-cards-view.svelte';
  import QuizView from './lib/QuizView.svelte';
  import { appState, loading } from './store.js';
  console.log($appState === 'editor');
</script>

<main>
  <div class="loading" class:hidden={!$loading}>
    <div class="lds-dual-ring" />
  </div>
  <div class={$appState === 'editor' ? '' : 'hidden'}>
    <Editor />
  </div>
  <div class={$appState === 'flashCards' ? '' : 'hidden'}>
    <FlashCardsView />
  </div>
  <div class={$appState === 'quiz' ? '' : 'hidden'}>
    <QuizView />
  </div>
</main>

<style>
  .lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
  }
  .lds-dual-ring:after {
    content: ' ';
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #fff;
    border-color: #fff transparent #fff transparent;
    animation: lds-dual-ring 1.2s linear infinite;
  }
  @keyframes lds-dual-ring {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  .loading {
    position: fixed;
    z-index: 99999;
    width: 100vw;
    height: 100vh;
    background-color: black;
    opacity: 0.4;
    top: 0%;
    left: 0%;
    font-size: 10rem;
    text-align: center;
    line-height: 100vh;
  }

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

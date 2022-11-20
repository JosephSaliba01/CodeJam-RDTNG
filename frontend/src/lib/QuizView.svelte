<script>
  import QuizCards from './QuizCards.svelte';
  import { appState } from '../store';
  let showEditor = () => appState.set('editor');
  import { tweened } from 'svelte/motion';
  let original = 1 * 60; // TYPE NUMBER OF SECONDS HERE
	let timer = tweened(original)

  // ------ dont need to modify code below
  // @ts-ignore
  import Typewriter from "svelte-typewriter";
  setInterval(() => {
    if ($timer > 0) $timer--;
  }, 1000);

  $: minutes = Math.floor($timer / 60);
  $: minname = minutes > 1 ? "mins" : "min";
  $: seconds = Math.floor($timer - minutes * 60)
</script>

<div>
  <button on:click={showEditor}>End quiz</button>
</div>

{#if $timer < 1}
  <h1>Time's up!</h1>
{:else}
  <h1><span class="mins">{minutes}</span>{minname} 

  <span class="secs">{seconds}</span>s!</h1>
  <progress value={$timer/original}></progress>
{/if}

<QuizCards />

<style>
  main {
    width: 600px;
    margin: 0 auto;
  }
	
	progress {
		display: block;
		width: 100%;
	}
	.mins {
		color: darkgoldenrod;
	}
	.secs {
		color: darkgoldenrod;
	}
  footer {
    margin-top: 3rem;
  }
  li {
    margin-bottom: 1rem;
  }
  .flex {
    display: flex;
    align-items: center;
  }
  .title {
    font-size: 2rem;
    font-weight: bold;
  }
</style>
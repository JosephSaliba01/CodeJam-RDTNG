<script>
    export let questions;
    import Card from './Card.svelte';
</script>

{#if Array.isArray($questions)}
    {#each $questions as question}
        <Card query={question.query} answer={question.answer} />
    {/each}
{/if}
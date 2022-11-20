<script>
    export let query;
    export let choices;
    export let answer;
</script>

<div id="quiz-card-main-view">
    <div id="quiz-card-question-view">
        <p>{query}</p>
    </div>
    <div id="quiz-card-choices-view">
        {#if Array.isArray(choices)}
            {#each choices as choice}
                <button class="quiz-card-choice-button">{choice}</button>
            {/each}
        {/if}
    </div>
</div>
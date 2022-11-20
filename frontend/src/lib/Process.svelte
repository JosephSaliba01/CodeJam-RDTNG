<script>
    export let note_name;
    export let notes_content;
    import Modal, {getModal} from './Modal.svelte';

    let selection
	
	// Callback function provided to the `open` function, it receives the value given to the `close` function call, or `undefined` if the Modal was closed with escape or clicking the X, etc.
	function setSelection(res){
		selection=res
	}
</script>

<div id="processing-view">
    <button on:click={()=>getModal().open()}>
        Open First Popup
    </button>
    <Modal>
        <h1>Hello {name}!</h1>
        <!-- opening a model with an `id` and specifying a callback	 -->
        <button on:click={()=>getModal('second').open(setSelection)}>
            Open Nested Popup
        </button>
        {#if selection}
        <p>
            Your selection was: {selection}
        </p>
        {/if}
    </Modal>
</div>


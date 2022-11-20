<script>
  import { not_equal } from 'svelte/internal';
  import { allNotes, currentNote, currentId, currentTitle } from '../store.js';

  let setCurrentNote = (note) => {
    console.log(note);
    currentNote.set(note);
    currentTitle.set(note.title);
  };

  let makeNewNote = () => {
    let storedArray = JSON.parse($allNotes);
    storedArray.push({
      id: $currentId,
      title: 'Note ' + $currentId,
      note: '',
      questions: [],
    });
    currentId.set($currentId + 1);
    currentNote.set(storedArray.at(-1));
    currentTitle.set($currentNote.title);
    allNotes.set(JSON.stringify(storedArray));
  };
</script>

<div id="storage-div">
  <button class="newNoteButton" on:click={makeNewNote}>+ New Note</button>
  <div class="noteButtonContainer">
    {#each JSON.parse($allNotes) as note}
      {#if note != null}
        <button class="noteButton" on:click={() => setCurrentNote(note)}
          >{note.title}</button
        >
      {/if}
    {/each}
  </div>
</div>

<style>
  #storage-div {
    background-color: rgb(232, 232, 232);
    margin-right: 0;
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
  }

  #storage-div > * {
    background-color: inherit;
  }

  #storage-div > * > * {
    background-color: inherit;
    color: rgb(93, 93, 93);
  }

  .newNoteButton {
    color: rgb(93, 93, 93);
    font-weight: 600;
    font-size: 20px;
  }

  .noteButtonContainer {
    display: flex;
    flex-direction: column;
    overflow: scroll;
    height: 80vh;
    margin: 0 !important;
    padding: 0 !important;
  }

  .noteButton {
    text-align: left;
    width: 100%;
  }
</style>

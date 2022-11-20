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
  .newNoteButton {
    background-color: rgb(31, 144, 31);
    color: white;
    font-weight: 600;
    font-size: 20px;
  }

  .noteButtonContainer {
    display: flex;
    flex-direction: column;
  }

  .noteButton {
    text-align: left;
    width: 100%;
  }
</style>

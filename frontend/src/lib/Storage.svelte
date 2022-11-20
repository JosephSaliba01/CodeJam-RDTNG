<script>
  import { not_equal } from 'svelte/internal';
  import { allNotes, currentNote, currentId } from '../store.js';

  let setCurrentNote = (note) => {
    console.log(note);
    currentNote.set(note);
  };

  let makeNewNote = () => {
    let storedArray = JSON.parse($allNotes);
    storedArray.push({
      id: $currentId,
      title: 'title',
      note: '',
      questions: [],
    });
    currentId.set($currentId + 1);
    currentNote.set(storedArray.at(-1));
    allNotes.set(JSON.stringify(storedArray));
  };
</script>

<div id="storage-div">
  <div id="storage-div-scrollable">
    <button class="newNoteButton" on:click={makeNewNote}>+ New Note</button>
    <div class="noteButtonContainer">
      {#each JSON.parse($allNotes) as note}
        <button class="noteButton" on:click={() => setCurrentNote(note)}
          >{note.title}</button
        >
      {/each}
    </div>
  </div>
</div>

<style>
  .newNoteButton {
    background-color: rgb(31, 144, 31);
    color: white;
    font-weight: 600;
    font-size: 20px;
  }

  .newNoteButton:hover {
    background-color: rgb(31, 117, 31);
  }

  .newNoteButton:active {
    background-color: rgb(24, 93, 24);
  }

  .noteButtonContainer {
    display: flex;
    flex-direction: column;
  }

  .noteButton {
    width: 100%;
  }
</style>

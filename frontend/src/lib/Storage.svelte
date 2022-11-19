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
      questions: '{}',
    });
    currentId.set($currentId + 1);
    allNotes.set(JSON.stringify(storedArray));
  };
</script>

<div id="storage-div">
  <div id="storage-div-scrollable">
    <button on:click={makeNewNote}>+ New Note</button>
    {#each JSON.parse($allNotes) as note}
      <button on:click={() => setCurrentNote(note)}>{note.title}</button>
    {/each}
  </div>
</div>

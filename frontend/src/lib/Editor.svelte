<script>
  // @ts-nocheck

  import { onMount, onDestroy } from 'svelte';
  import { Editor } from '@tiptap/core';
  import StarterKit from '@tiptap/starter-kit';
  import CharacterCount from '@tiptap/extension-character-count';
  import { text } from 'svelte/internal';
  import { questions } from '../store.js';
  import Cards from './Cards.svelte';
  import Dropzone from 'svelte-file-dropzone';
  import { allNotes } from '../store';
  let element;
  let editor;

  // Stop default drag and drop behaviour
  window.addEventListener(
    'dragover',
    function (e) {
      e = e || event;
      e.preventDefault();
    },
    false
  );
  window.addEventListener(
    'drop',
    function (e) {
      e = e || event;
      e.preventDefault();
    },
    false
  );

  onMount(() => {
    editor = new Editor({
      element: element,
      extensions: [StarterKit, CharacterCount],
      content: '',
      autofocus: true,
      editable: true,
      onTransaction: () => {
        // force re-render so `editor.isActive` works as expected
        editor = editor;
      },
    });
  });

  onDestroy(() => {
    if (editor) {
      editor.destroy();
    }
  });

  let generateQuestions = async (data) => {
    // Clean up to only send final string
    let paragraphs = data.content;
    let string = '';
    paragraphs.forEach((element) => {
      let paragraph = element.content;
      if (!(paragraph == undefined)) {
        string += paragraph[0].text + ' ';
      }
    });

    const response = await fetch('http://127.0.0.1:5000/content', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: string,
    });

    let responseJson = await response.json();

    let storedArray = JSON.parse($allNotes);
    storedArray.push({
      title: 'title',
      note: string,
      questions: responseJson.questions,
    });
    allNotes.set(JSON.stringify(storedArray));

    questions.set(responseJson.questions);
  };

  async function handleFilesSelect(e) {
    let file = e.dataTransfer.files[0];
    let fileContent = await file.text();
    fileContent = fileContent.replaceAll(/\r?\n|\r/g, '<br>');
    console.log(fileContent);
    editor.commands.setContent(fileContent);
  }
</script>

{#if editor}
  <!--  <button-->
  <!--          on:click={() => editor.chain().focus().toggleHeading({ level: 1}).run()}-->
  <!--          class:active={editor.isActive('heading', { level: 1 })}-->
  <!--  >-->
  <!--    H1-->
  <!--  </button>-->
  <!--  <button-->
  <!--          on:click={() => editor.chain().focus().toggleHeading({ level: 2 }).run()}-->
  <!--          class:active={editor.isActive('heading', { level: 2 })}-->
  <!--  >-->
  <!--    H2-->
  <!--  </button>-->
  <!--  <button on:click={() => editor.chain().focus().setParagraph().run()} class:active={editor.isActive('paragraph')}>-->
  <!--    P-->
  <!--  </button>-->
{/if}


<div id="main-view">
  <div id="editor-header">
    <div id="controls">

    </div>
    {#if editor}
      <button style="margin-left: auto;" on:click={generateQuestions(editor.getJSON())}>Generate Questions</button>
    {/if}
  </div>
  <div id="editor-main">
    <div id="storage-div">
      <div id="storage-div-scrollable">
        
      </div>
    </div>
    <div id="editor-div" bind:this={element} on:drop={handleFilesSelect}>
      <div id="format-div">
        <button on:click={editor.chain().focus().toggleBold().run()}>
      </div>
      <hr>
    </div>
  </div>
</div>

{#if editor}
  <p>{editor.storage.characterCount.words()} words</p>
{/if}

<Cards {questions} />

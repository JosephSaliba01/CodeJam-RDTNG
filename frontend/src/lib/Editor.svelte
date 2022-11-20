<script>
  // @ts-nocheck

  import Bold from '@tiptap/extension-bold';
  import Highlight from '@tiptap/extension-highlight';
  import { onMount, onDestroy } from 'svelte';
  import { Editor } from '@tiptap/core';
  import StarterKit from '@tiptap/starter-kit';
  import CharacterCount from '@tiptap/extension-character-count';
  import { text } from 'svelte/internal';
  import {
    currentNote,
    currentId,
    allNotes,
    appState,
    currentTitle,
    loading,
    current_FC_index,
    current_Q_index
  } from '../store';

  import Storage from './Storage.svelte';
  import app from '../main';
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
      extensions: [StarterKit, CharacterCount, Bold, Highlight],
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
    unsubscribeToCurrentNote();
  });

  let generateQuestions = async (data) => {
    loading.set(true);

    // Clean up to only send final string
    let paragraphs = data.content;

    let array_of_paragraphs = [];

    paragraphs.forEach((element) => {
      let paragraph = element.content;
      if (!(paragraph == undefined)) {
        array_of_paragraphs.push(paragraph[0].text);
      }
    });

    const response = await fetch('http://127.0.0.1:5000/content', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(array_of_paragraphs),
    });

    let responseJson = await response.json();

    let storedArray = JSON.parse($allNotes);
    // If there is no note selected, e.g., the user just opened the app
    // Create a new one
    if ($currentNote == null) {
      storedArray.push({
        id: parseInt($currentId),
        title: $currentTitle,
        note: '',
        questions: [],
      });
      currentId.set(parseInt($currentId + 1));
      currentNote.set(storedArray.at(-1));
      $currentNote.note = data;
      $currentNote.questions = responseJson.questions;
    }
    // If there is a note selected, overwrite it
    else {
      $currentNote.note = data;
      $currentNote.questions = responseJson.questions;
      $currentNote.title = $currentTitle;
      storedArray[$currentNote.id] = $currentNote;
    }

    allNotes.set(JSON.stringify(storedArray));

    loading.set(false);
  };

  async function handleFilesSelect(e) {
    let file = e.dataTransfer.files[0];
    let fileContent = await file.text();
    fileContent = fileContent.replaceAll(/\r?\n|\r/g, '<br>');
    console.log(fileContent);
    editor.commands.setContent(fileContent);
  }

  const unsubscribeToCurrentNote = currentNote.subscribe((value) => {
    if (value != null) editor.commands.setContent(value.note);
  });

  let enterQuizView = () => {
    current_Q_index.set(0);
    appState.set('quiz');
  };

  let enterFlashCardsView = () => {
    current_FC_index.set(0);
    appState.set('flashCards');
  };
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
    <div id="controls" />
    {#if editor}
      <button
        disabled={$currentNote == null || $currentNote.questions.length <= 0}
        on:click={enterQuizView}
      >
        Take quiz
      </button>
      <button
        class="topButton"
        disabled={$currentNote == null || $currentNote.questions.length <= 0}
        on:click={enterFlashCardsView}
      >
        Flash cards
      </button>
      <button class="topButton" on:click={generateQuestions(editor.getJSON())}
        >Generate Questions</button
      >
    {/if}
  </div>
  <div id="editor-main">
    <Storage />
    <div id="editor-div" bind:this={element} on:drop={handleFilesSelect}>
      <input type="text" bind:value={$currentTitle} class="title" />
      <div id="format-div">
        {#if editor}
          <button
            on:click={editor.chain().focus().toggleHeading({ level: 1 }).run()}
            class="format_button {editor.isActive('heading', { level: 1 })
              ? 'is_button_active'
              : 'is_button_inactive'}"
          >
            <p>H1</p>
          </button>
          <button
            on:click={editor.chain().focus().toggleHeading({ level: 2 }).run()}
            class="format_button {editor.isActive('heading', { level: 2 })
              ? 'is_button_active'
              : 'is_button_inactive'}"
          >
            <p>H2</p>
          </button>
          <button
            on:click={editor.chain().focus().toggleBold().run()}
            class="format_button {editor.isActive('bold')
              ? 'is_button_active'
              : 'is_button_inactive'}"
          >
            <p style="font-weight: 700;">B</p>
          </button>
          <button
            on:click={editor.chain().focus().toggleItalic().run()}
            class="format_button {editor.isActive('italic')
              ? 'is_button_active'
              : 'is_button_inactive'}"
          >
            <p style="font-style:italic">I</p>
          </button>
          <button
            on:click={editor.chain().focus().toggleHighlight().run()}
            class="format_button {editor.isActive('highlight')
              ? 'is_button_active'
              : 'is_button_inactive'}"
          >
            <p style="font-style:italic">h</p>
          </button>
        {/if}
      </div>
      <hr />
    </div>
  </div>
</div>

{#if editor}
  <p>{editor.storage.characterCount.words()} words</p>
{/if}

<style>
  #editor-div {
    text-align: left;
  }

  .title {
    box-sizing: border-box;
    font-size: 2rem;
    width: 100%;
    margin-top: 1rem;
    border-radius: 10px;
    border-style: solid;
    font-weight: 600;
  }

  #editor-header {
    display: flex;
    gap: 2%;
  }

  .topButton {
    min-height: 50px;
  }

  #controls {
    min-height: 50px;
  }
</style>

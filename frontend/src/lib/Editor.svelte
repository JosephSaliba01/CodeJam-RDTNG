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
    current_Q_index,
  } from '../store';

  import Storage from './Storage.svelte';
  import app from '../main';
  import Process from './Process.svelte';
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
      extensions: [
        StarterKit.configure({
          listItem: false,
          bulletList: false,
          orderedList: false,
          codeBlock: false,
          blockquote: false,
        }),

        CharacterCount,
        Bold,
        Highlight,
      ],
      content: '',
      autofocus: true,
      editable: true,
      disablePasteRules: true,
      disableInputRules: true,
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
    console.log(data);

    loading.set(true);

    // Clean up to only send final string
    let paragraphs = data.content;

    let array_of_paragraphs = [];

    paragraphs.forEach((element) => {
      if (element.type == 'paragraph') {
        let paragraph = element.content;
        if (!(paragraph == undefined)) {
          array_of_paragraphs.push(paragraph[0].text);
        }
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

  let deleteNote = () => {
    let storedArray = JSON.parse($allNotes);
    var removeIndex = storedArray
      .map((item) => {
        if (item != null) return item.id;
      })
      .indexOf($currentNote.id);
    removeIndex >= 0 && storedArray.splice(removeIndex, 1);
    allNotes.set(JSON.stringify(storedArray));
    currentNote.set(null);
    editor.commands.setContent('');
    currentTitle.set('Note ' + $currentId);
  };
</script>

<div id="main-view">
  <div id="editor-header">
    <div id="controls" />
    {#if editor}{/if}
  </div>
  <div id="editor-main">
    <Storage />
    <div id="editor-div" bind:this={element} on:drop={handleFilesSelect}>
      <div id="title-div">
        <input type="text" bind:value={$currentTitle} class="title" />
        <button
          on:click={deleteNote}
          class="delete_button {$currentNote == null ? 'hidden' : ''}"
          >🗑️
        </button>
        <button
          class="topButton enterQuizButton"
          disabled={$currentNote == null || $currentNote.questions.length <= 0}
          on:click={enterQuizView}
        >
          Take quiz
        </button>
        <button
          class="topButton enterFlashCardsButton"
          disabled={$currentNote == null || $currentNote.questions.length <= 0}
          on:click={enterFlashCardsView}
        >
          Flash cards
        </button>
        <button
          class="topButton saveButton"
          on:click={generateQuestions(editor.getJSON())}
          >Save and Generate</button
        >
      </div>
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

          <p class="wordCount">
            {editor.storage.characterCount.words()}
            {editor.storage.characterCount.words() === 1 ? 'word' : 'words'}
          </p>
        {/if}
      </div>
      <hr />
    </div>
  </div>
</div>

<style>
  .saveButton {
    background-color: rgb(157, 228, 254);
  }

  .enterFlashCardsButton:enabled {
    background-color: rgb(157, 254, 193);
  }

  .enterQuizButton:enabled {
    background-color: rgb(157, 254, 193);
  }

  #title-div {
    display: flex;
    gap: 0.2rem;
    align-items: center;
    padding: 0;
  }

  #title-div > button {
    min-height: 3rem;
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .wordCount {
    margin-left: 1rem;
    font-size: 14px;
  }

  .hidden {
    visibility: hidden;
  }

  .delete_button {
    margin-left: auto;
    height: 3rem;
    width: 3rem;
    font-size: 1rem;
  }

  #editor-div {
    text-align: left;
  }

  .title {
    box-sizing: border-box;
    font-size: 2rem;
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

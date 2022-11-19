<script>
// @ts-nocheck

  import { onMount, onDestroy } from 'svelte'
  import { Editor } from '@tiptap/core'
  import StarterKit from '@tiptap/starter-kit'
  import CharacterCount from '@tiptap/extension-character-count'

  let element
  let editor

  onMount(() => {
    editor = new Editor({
      element: element,
      extensions: [
        StarterKit,
        CharacterCount
      ],
      content: '',
      autofocus: true,
      editable: true,
      onTransaction: () => {
        // force re-render so `editor.isActive` works as expected
        editor = editor
      },
    })
  })

  onDestroy(() => {
    if (editor) {
      editor.destroy()
    }
  })

  let generateQuestions = async (data) => {
    const response = await fetch('http://127.0.0.1:5000/content', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
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

<div bind:this={element}></div>

{#if editor}
  <p>{editor.storage.characterCount.words()} words</p>
  <button on:click={generateQuestions(editor.getJSON())}>Generate Questions</button>
{/if}
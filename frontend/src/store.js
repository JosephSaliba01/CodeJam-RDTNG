import { writable } from 'svelte/store';

export const currentNote = writable(null);
export const appState = writable('editor');

// Get the value out of storage on load.
export const allNotes = writable(localStorage.allNotes || '[]');
export const currentId = writable(parseInt(localStorage.currentId) || 0);

// Anytime the store changes, update the local storage value.
allNotes.subscribe((value) => (localStorage.allNotes = value));
currentId.subscribe((value) => (localStorage.currentId = value));

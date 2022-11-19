import { writable } from 'svelte/store';

export const questions = writable(null);

// Get the value out of storage on load.
export const allNotes = writable(localStorage.allNotes || '[]');

// Anytime the store changes, update the local storage value.
allNotes.subscribe((value) => (localStorage.allNotes = value));

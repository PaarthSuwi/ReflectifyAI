<template>
  <div class="prompt-selector-container">
    <label class="prompt-label">Select a Reflection Prompt</label>
    <div class="select-wrapper">
      <select v-model="selectedPrompt" @change="emitPrompt" class="input-field styled-select">
        <option disabled value="">✨ Need inspiration? Choose a prompt...</option>
        <option v-for="prompt in prompts" :key="prompt" :value="prompt">
          {{ prompt }}
        </option>
      </select>
      <div class="select-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="6 9 12 15 18 9"></polyline>
        </svg>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['prompt-selected'])

const selectedPrompt = ref('')
const prompts = [
  "What did you learn from this project?",
  "What challenges did you face and how did you overcome them?",
  "What would you do differently next time?",
  "Summarize your experience in 100 words.",
  "How did this task contribute to your growth?"
]

const emitPrompt = () => {
  emit('prompt-selected', selectedPrompt.value)
  setTimeout(() => { selectedPrompt.value = '' }, 500) // Reset after inserting
}
</script>

<style scoped>
.prompt-selector-container {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.prompt-label {
  font-weight: 500;
  color: #a3b3c4;
  font-size: 0.9rem;
}

.select-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.styled-select {
  appearance: none;
  cursor: pointer;
  padding-right: 2.5rem;
  background-color: rgba(0, 0, 0, 0.3);
}

.styled-select option {
  background-color: var(--bg-color);
  color: var(--text-primary);
}

.select-icon {
  position: absolute;
  right: 1rem;
  pointer-events: none;
  color: var(--text-secondary);
}
</style>

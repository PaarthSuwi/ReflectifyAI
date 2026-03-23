<template>
  <div class="analysis-viewer animate-fade-in">
    
    <div class="analysis-section">
      <h3>Key Takeaways 💡</h3>
      <ul class="styled-list">
        <li v-for="(item, idx) in analysis.key_takeaways" :key="'kt-'+idx">
          <div class="bullet"></div>
          <p>{{ item }}</p>
        </li>
      </ul>
    </div>

    <div class="analysis-section two-col">
      <div class="sub-section">
        <h3>Skills Developed 🛠️</h3>
        <ul class="styled-list">
          <li v-for="(skill, idx) in analysis.skills_developed" :key="'sd-'+idx">
            <div class="bullet"></div>
            <p>{{ skill }}</p>
          </li>
        </ul>
      </div>
      <div class="sub-section">
        <h3>Suggested Next Steps 🚀</h3>
        <ul class="styled-list">
          <li v-for="(step, idx) in analysis.suggested_next_steps" :key="'sn-'+idx">
            <div class="bullet"></div>
            <p>{{ step }}</p>
          </li>
        </ul>
      </div>
    </div>
    
    <div class="difficulty-section">
      <div class="diff-header">
        <span>Project Complexity Rating: </span>
        <strong>{{ analysis.difficulty_rating }} / 10</strong>
      </div>
      <div class="progress-bar">
        <div class="progress-fill" :style="{ width: (analysis.difficulty_rating * 10) + '%' }"></div>
      </div>
    </div>

    <div class="analysis-section latex-section">
      <div class="latex-header">
        <h3>Formatted LaTeX Report 📄</h3>
        <button class="btn-copy" @click="copyLatex">
          {{ copied ? 'Copied!' : 'Copy LaTeX' }}
        </button>
      </div>
      <pre class="latex-code"><code>{{ analysis.latex_report }}</code></pre>
    </div>
    
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  analysis: {
    type: Object,
    required: true
  }
})

const copied = ref(false)

const copyLatex = () => {
  navigator.clipboard.writeText(props.analysis.latex_report)
    .then(() => {
      copied.value = true
      setTimeout(() => { copied.value = false }, 2000)
    })
    .catch(err => {
      console.error('Failed to copy: ', err)
    })
}
</script>

<style scoped>
.analysis-viewer {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.analysis-section {
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.5rem;
}

.two-col {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

@media (min-width: 600px) {
  .two-col {
    flex-direction: row;
    gap: 2rem;
  }
  .sub-section {
    flex: 1;
  }
}

h3 {
  font-size: 1.1rem;
  color: var(--accent-color);
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0;
}

.styled-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.styled-list li {
  display: flex;
  gap: 0.75rem;
  align-items: flex-start;
  font-size: 0.95rem;
  line-height: 1.5;
  color: #f2ebe5;
}

.bullet {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent-glow);
  margin-top: 0.45rem;
  flex-shrink: 0;
}

.difficulty-section {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  background: rgba(209, 155, 113, 0.1);
  padding: 1rem 1.5rem;
  border-radius: 8px;
  border-left: 4px solid var(--accent-color);
}

.diff-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.difficulty-section span {
  font-size: 0.95rem;
  color: var(--text-secondary);
}

.difficulty-section strong {
  font-size: 1.2rem;
  color: var(--text-primary);
}

.progress-bar {
  height: 6px;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 3px;
  overflow: hidden;
  margin-top: 0.5rem;
}

.progress-fill {
  height: 100%;
  background: var(--gradient-primary);
  border-radius: 3px;
  transition: width 1s ease-in-out;
}

.latex-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.latex-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.latex-header h3 {
  margin: 0;
}

.btn-copy {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.btn-copy:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: var(--accent-color);
}

.latex-code {
  background: #110e0c;
  padding: 1rem;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  font-family: monospace;
  font-size: 0.85rem;
  overflow-x: auto;
  white-space: pre-wrap;
  color: #c9b9af;
  line-height: 1.5;
  max-height: 400px;
  overflow-y: auto;
  margin: 0;
}
</style>

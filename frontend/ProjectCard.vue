<template>
  <div class="project-card glass-panel animate-fade-in">
    <div class="card-header">
      <div class="project-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
        </svg>
      </div>
      <h3 class="gradient-text">{{ project.title }}</h3>
    </div>
    
    <p class="project-desc">{{ project.description || 'No description provided.' }}</p>
    
    <div v-if="reflections && reflections.length > 0" class="reflections-container">
      <h4 class="reflections-title">Insights</h4>
      <ul class="reflections-list">
        <li v-for="reflection in reflections" :key="reflection.id" class="reflection-item">
          <div class="reflection-bullet"></div>
          <p>{{ reflection.summary }}</p>
        </li>
      </ul>
    </div>
    <div v-else class="reflections-empty">
      <p>No reflections yet.</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  project: {
    type: Object,
    required: true
  },
  reflections: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.project-card {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.3);
  border-color: rgba(88, 166, 255, 0.4);
}

.card-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.project-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: rgba(31, 111, 235, 0.1);
  color: var(--accent-color);
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-header h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.project-desc {
  color: var(--text-secondary);
  font-size: 0.95rem;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.reflections-container {
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px dashed var(--border-color);
}

.reflections-title {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #a3b3c4;
  margin-bottom: 0.75rem;
}

.reflections-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.reflection-item {
  display: flex;
  gap: 0.5rem;
  align-items: flex-start;
}

.reflection-bullet {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent-color);
  margin-top: 0.4rem;
  flex-shrink: 0;
}

.reflection-item p {
  font-size: 0.9rem;
  color: #c9d1d9;
  line-height: 1.5;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.reflections-empty {
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px dashed var(--border-color);
  font-size: 0.85rem;
  color: var(--text-secondary);
  font-style: italic;
}
</style>

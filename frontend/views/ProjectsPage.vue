<template>
  <div class="projects-page animate-fade-in">
    <header class="page-header">
      <h1 class="gradient-text">My Projects Archive</h1>
      <p class="subtitle">Review your past experiences and AI reflections</p>
    </header>

    <div v-if="loading" class="state-container loading-state">
      <div class="loader"></div>
      <p>Loading your timeline...</p>
    </div>
    
    <div v-else-if="projects.length === 0" class="state-container empty-state">
      <div class="empty-icon">📁</div>
      <p>Your archive is empty. Head to the dashboard to document your first project!</p>
      <router-link to="/dashboard" class="btn-primary mt-4 inline-block">Go to Dashboard</router-link>
    </div>
    
    <div v-else class="projects-grid">
      <ProjectCard
        v-for="project in projects"
        :key="project.id"
        :project="project"
        :reflections="project.reflections || []"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ProjectCard from '../ProjectCard.vue'

const projects = ref([])
const loading = ref(true)
const userId = 1 // 🟡 Replace with dynamic user authentication if needed

onMounted(async () => {
  try {
    const res = await axios.get(`http://localhost:8000/api/projects/${userId}`)
    projects.value = res.data
  } catch (err) {
    console.error('Error fetching projects:', err)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.projects-page {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.page-header {
  margin-bottom: 1rem;
}

.page-header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.state-container {
  min-height: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: var(--surface-color);
  border: 1px dashed var(--border-color);
  border-radius: 12px;
  text-align: center;
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
  opacity: 0.7;
}

.mt-4 {
  margin-top: 1.5rem;
}

.inline-block {
  display: inline-block;
  text-decoration: none;
}

.loader {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(88, 166, 255, 0.2);
  border-radius: 50%;
  border-top-color: var(--accent-color);
  animation: spin 1s ease-in-out infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>

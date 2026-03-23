<template>
  <div class="summary-viewer animate-fade-in">
    <div class="summary-header">
      <div class="summary-icon">✨</div>
      <h3>Refined Insights</h3>
    </div>
    <div class="summary-content">
      <p>{{ summary }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  summary: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.summary-viewer {
  background: rgba(31, 111, 235, 0.05);
  border: 1px solid var(--accent-glow);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.summary-viewer:hover {
  box-shadow: 0 8px 32px rgba(31, 111, 235, 0.15);
  border-color: rgba(88, 166, 255, 0.6);
}

.summary-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.5rem;
  background: rgba(0, 0, 0, 0.2);
  border-bottom: 1px solid var(--border-color);
}

.summary-icon {
  font-size: 1.25rem;
}

.summary-header h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.summary-content {
  padding: 1.5rem;
  line-height: 1.7;
  color: #c9d1d9;
  font-size: 1.05rem;
}
</style>

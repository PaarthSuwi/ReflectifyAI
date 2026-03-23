<template>
  <div id="app" class="app-container">
    <nav class="glass-nav">
      <div class="nav-content">
        <div class="logo">
          <span class="gradient-text fw-bold">Reflectify</span>
          <span class="logo-ai">.ai</span>
        </div>
        <div class="nav-links">
          <router-link to="/dashboard" class="nav-item">Dashboard</router-link>
          <router-link to="/projects" class="nav-item">My Projects</router-link>
        </div>
        <div class="user-profile">
          <div class="avatar">
            <span>TA</span>
          </div>
        </div>
      </div>
    </nav>
    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.glass-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--surface-color);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-color);
  padding: 1rem 0;
}

.nav-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.fw-bold {
  font-weight: 700;
}

.logo-ai {
  color: var(--accent-color);
  font-weight: 300;
}

.nav-links {
  display: flex;
  gap: 2rem;
  align-items: center;
}

.nav-item {
  color: var(--text-secondary);
  text-decoration: none;
  font-weight: 500;
  font-size: 1rem;
  transition: all 0.3s ease;
  position: relative;
}

.nav-item:hover, .router-link-active {
  color: var(--text-primary);
}

.router-link-active::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--gradient-primary);
  border-radius: 2px;
}

.user-profile {
  display: flex;
  align-items: center;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--gradient-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  color: white;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(31, 111, 235, 0.3);
  transition: transform 0.3s ease;
}

.avatar:hover {
  transform: scale(1.05);
}

.main-content {
  flex: 1;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 3rem 2rem;
}

/* Page Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>

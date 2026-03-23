<template>
  <div class="dashboard-container animate-fade-in">
    <header class="dashboard-header">
      <h1 class="gradient-text">Welcome back, User</h1>
      <p class="subtitle">Document, reflect, and grow with AI-powered insights.</p>
    </header>

    <div class="dashboard-grid">
      <!-- Left Column: Input Form -->
      <section class="glass-panel input-section">
        <h2 class="section-title">New Reflection</h2>
        
        <PromptSelector @prompt-selected="insertPrompt" />

        <form @submit.prevent="submitReflection" class="reflection-form">
          <div class="form-group">
            <label for="title">Title</label>
            <input 
              id="title"
              v-model="title" 
              class="input-field" 
              placeholder="e.g. Completed Phase 1 of AI Project" 
              required 
            />
          </div>
          
          <div class="form-group">
            <label>Project Materials (Optional)</label>
            
            <!-- File Upload UI -->
            <div class="file-upload-wrapper">
              <input type="file" ref="fileInput" @change="handleFileChange" accept=".pdf,image/*" multiple class="hidden-input" />
              <div v-if="selectedFiles.length === 0" class="upload-dropzone" @click="$refs.fileInput.click()">
                <div class="upload-icon">📄</div>
                <p>Click to upload PDFs or Images</p>
                <span class="upload-hint">Supports .pdf, .png, .jpg (Multiple allowed)</span>
              </div>
              <div v-else class="files-selected">
                <div v-for="(file, idx) in selectedFiles" :key="idx" class="file-item">
                  <div class="file-info">
                    <span class="file-icon">✅</span>
                    <span class="file-name">{{ file.name }}</span>
                  </div>
                  <button type="button" class="btn-remove" @click.stop="removeFile(idx)">✖</button>
                </div>
                <button type="button" class="btn-add-more" @click="$refs.fileInput.click()">+ Add More Files</button>
              </div>
            </div>

            <div class="or-divider"><span>OR WRITE IT MANUALLY</span></div>
            
            <textarea
              id="content"
              v-model="inputText"
              class="input-field textarea-field"
              placeholder="Describe what you worked on, challenges faced, and what you learned textually..."
              :required="selectedFiles.length === 0"
            ></textarea>
          </div>
          
          <div class="form-group format-group">
            <label>Output Format</label>
            <select v-model="outputFormat" class="input-field styled-select">
              <option value="default">✨ Default UI Report</option>
              <option value="latex">📄 Generate LaTeX Source</option>
              <option value="docx">📝 Download Word Document</option>
              <option value="pdf">📕 Download PDF Document</option>
            </select>
          </div>

          <button type="submit" class="btn-primary submit-btn" :disabled="isSubmitting">
            <span v-if="!isSubmitting">✨ Analyze & Summarize</span>
            <span v-else class="loader"></span>
          </button>
        </form>
      </section>

      <!-- Right Column: AI Output -->
      <section class="glass-panel summary-section">
        <h2 class="section-title">AI Insights & Report</h2>
        <div v-if="!summary && !analysisData && !isSubmitting" class="empty-state">
          <div class="empty-icon">✨</div>
          <p>Submit a reflection or upload files to generate AI insights.</p>
        </div>
        <div v-else-if="isSubmitting" class="loading-state">
          <div class="loader-large"></div>
          <p>Gemini AI is analyzing your experience...</p>
        </div>
        
        <!-- Standard text summary -->
        <SummaryViewer v-else-if="summary" :summary="summary" />
        
        <!-- Structured File Analysis -->
        <AnalysisViewer v-else-if="analysisData" :analysis="analysisData" />
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard'
}
</script>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import PromptSelector from '../PromptSelector.vue'
import SummaryViewer from '../SummaryViewer.vue'
import AnalysisViewer from '../AnalysisViewer.vue'

const title = ref('')
const inputText = ref('')
const summary = ref('')
const analysisData = ref(null)
const isSubmitting = ref(false)
const selectedFiles = ref([])
const fileInput = ref(null)
const outputFormat = ref('default')

const insertPrompt = (prompt) => {
  inputText.value = prompt + '\n\n' + inputText.value
}

const handleFileChange = (e) => {
  const files = e.target.files
  if (files) {
    for (let i = 0; i < files.length; i++) {
        selectedFiles.value.push(files[i])
    }
  }
}

const removeFile = (index) => {
  selectedFiles.value.splice(index, 1)
  if (fileInput.value) fileInput.value.value = ''
}

const downloadBase64File = (base64Data, format) => {
    const link = document.createElement('a');
    let mimeType = 'application/pdf';
    let ext = '.pdf';
    
    if (format === 'docx') {
        mimeType = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document';
        ext = '.docx';
    }
    
    link.href = `data:${mimeType};base64,${base64Data}`;
    link.download = `Project_Report${ext}`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

const submitReflection = async () => {
  if (!title.value || (!inputText.value && selectedFiles.value.length === 0)) return;
  
  isSubmitting.value = true
  summary.value = ''
  analysisData.value = null
  
  try {
    if (selectedFiles.value.length > 0) {
      // Handle Multi-File Upload
      const formData = new FormData()
      selectedFiles.value.forEach(file => {
          formData.append('files', file)
      })
      if (title.value) formData.append('project_title', title.value)
      
      // Add the format
      formData.append('output_format', outputFormat.value)
      
      const response = await axios.post('http://localhost:8000/api/ai/upload_and_analyze', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      
      if (response.data.download_data) {
          downloadBase64File(response.data.download_data, response.data.format)
      }
      
      if (response.data.analysis) {
        analysisData.value = response.data.analysis
        title.value = ''
        inputText.value = ''
        selectedFiles.value = []
      }
    } else {
      // Handle old text summarize
      const response = await axios.post('http://localhost:8000/api/ai/summarize', {
        text: inputText.value, project_title: title.value, save_to_project: true
      })
      if (response.data.summary) {
        summary.value = response.data.summary; title.value = ''; inputText.value = ''
      } else summary.value = 'Could not generate summary.'
    }
  } catch (err) {
    console.error(err); alert('An error occurred. Check backend console.')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
.dashboard-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.dashboard-header { margin-bottom: 1rem; }
.dashboard-header h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
.subtitle { color: var(--text-secondary); font-size: 1.1rem; }
.dashboard-grid { display: grid; grid-template-columns: 1fr; gap: 2rem; }

@media (min-width: 900px) {
  .dashboard-grid { grid-template-columns: 1.1fr 0.9fr; }
}

.input-section, .summary-section { padding: 2rem; display: flex; flex-direction: column; gap: 1.5rem; }
.section-title { font-size: 1.25rem; font-weight: 600; border-bottom: 1px dashed var(--border-color); padding-bottom: 1rem; margin-bottom: 0.5rem; }
.reflection-form { display: flex; flex-direction: column; gap: 1.5rem; }
.form-group { display: flex; flex-direction: column; gap: 0.5rem; }
.form-group label { font-weight: 600; color: var(--accent-color); font-size: 0.9rem; letter-spacing: 0.05em; text-transform: uppercase; }
.textarea-field { min-height: 150px; resize: vertical; line-height: 1.6; }

/* File Upload Styles */
.hidden-input { display: none; }
.upload-dropzone {
  border: 2px dashed rgba(209, 155, 113, 0.4);
  background: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
}
.upload-dropzone:hover {
  background: rgba(209, 155, 113, 0.05);
  border-color: var(--accent-color);
}
.upload-icon { font-size: 2rem; margin-bottom: 0.5rem; opacity: 0.8; }
.upload-dropzone p { color: var(--text-primary); font-weight: 500; margin-bottom: 0.25rem; }
.upload-hint { font-size: 0.8rem; color: var(--text-secondary); }

.file-selected {
  border: 1px solid var(--accent-color);
  background: rgba(209, 155, 113, 0.1);
  border-radius: 8px;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
}
.file-info { display: flex; align-items: center; gap: 0.5rem; }
.file-name { font-weight: 600; color: var(--text-primary); word-break: break-all; }
.btn-remove { background: transparent; border: none; color: var(--text-secondary); cursor: pointer; font-size: 1.2rem; transition: color 0.3s; }
.btn-remove:hover { color: #ff5e5e; }

.or-divider {
  display: flex; align-items: center; margin: 0.5rem 0; color: var(--text-secondary); font-size: 0.8rem; font-weight: 600; text-transform: uppercase;
}
.or-divider::before, .or-divider::after {
  content: ''; flex: 1; border-bottom: 1px dashed var(--border-color);
}
.or-divider span { padding: 0 1rem; }

.submit-btn { margin-top: 1rem; display: flex; justify-content: center; align-items: center; min-height: 52px; }
.empty-state, .loading-state { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; color: var(--text-secondary); min-height: 300px; background: rgba(0, 0, 0, 0.1); border-radius: 8px; border: 1px dashed var(--border-color); }
.empty-icon { font-size: 3rem; margin-bottom: 1rem; opacity: 0.5; }

.loader, .loader-large {
  display: inline-block;
  border-radius: 50%;
  animation: spin 1s ease-in-out infinite;
}
.loader { width: 24px; height: 24px; border: 3px solid rgba(255, 255, 255, 0.3); border-top-color: white; }
.loader-large { width: 48px; height: 48px; border: 4px solid rgba(209, 155, 113, 0.2); border-top-color: var(--accent-color); margin-bottom: 1rem; }

@keyframes spin { to { transform: rotate(360deg); } }
</style>

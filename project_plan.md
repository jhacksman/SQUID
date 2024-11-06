# Project Plan: Open Source Computer Vision Assistant

## System Architecture Overview

### Components
1. **Nemotron-70B LLM**
   - Deployment Configuration:
     - INT4 AWQ quantization (~35GB total)
     - 3-way tensor parallelism across 3090s (~11.67GB per GPU)
     - PAGED_KV_CACHE for memory efficiency
     - ~12.33GB per GPU available for activations and KV cache
   - Role: Main reasoning engine and instruction processing

2. **Molmo Vision System**
   - Components:
     - ViT image encoder
     - Connector module
     - Decoder-only Transformer
   - Role: Screenshot analysis and feature detection

3. **Interactive Interface**
   - Web-based UI for text input
   - Screenshot capture system
   - Response display

### Integration Flow
1. User inputs text instruction through UI
2. System captures screen using system APIs
3. Molmo processes screenshot to identify UI elements and features
4. Nemotron-70B receives:
   - User instruction
   - Molmo's feature analysis
   - Context window (4K tokens)
5. LLM generates response/action plan
6. System executes actions or displays response

### Memory Management
- Total VRAM: 64GB (3x RTX 3090 24GB)
- Allocation:
  - Nemotron-70B: ~35GB (distributed)
  - Molmo: Remaining VRAM (~29GB)
  - Dynamic KV cache management

### Technical Implementation
1. **Model Deployment**
   - TensorRT-LLM for Nemotron-70B optimization
   - INT4 AWQ quantization
   - Tensor parallelism across GPUs

2. **Vision Processing**
   - Molmo for feature detection
   - Screenshot preprocessing pipeline
   - Feature extraction and encoding

3. **System Integration**
   - FastAPI backend
   - WebSocket for real-time communication
   - Screenshot capture service
   - Action execution system

### Development Phases
1. **Phase 1: Model Setup**
   - Deploy Nemotron-70B with quantization
   - Integrate Molmo vision system
   - Validate VRAM usage

2. **Phase 2: Core Features**
   - Implement screenshot capture
   - Develop UI element detection
   - Create basic interaction system

3. **Phase 3: Integration**
   - Connect all components
   - Implement action execution
   - Add safety measures

4. **Phase 4: Optimization**
   - Fine-tune performance
   - Optimize memory usage
   - Improve response time

### Safety and Limitations
1. **Access Control**
   - Restricted system access
   - Action verification
   - User confirmation for critical operations

2. **Resource Management**
   - VRAM monitoring
   - Load balancing
   - Error handling

3. **Known Limitations**
   - GPU memory constraints
   - Processing latency
   - Action scope restrictions

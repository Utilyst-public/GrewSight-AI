# Utilyst Mobile App - UI/UX Design Documentation

## Overview
This document outlines the complete mobile interface design for the Utilyst troubleshooting assistant application, including user flows, design decisions, and technical specifications.

---

## Design Philosophy

### Core Principles
1. **Simplicity First**: Field technicians need quick, distraction-free access to solutions
2. **Visual Clarity**: Large touch targets, high contrast, and readable text for outdoor use
3. **Guided Experience**: Step-by-step flows that reduce cognitive load
4. **Context Awareness**: Smart defaults and suggestions based on user behavior
5. **Offline Capable**: Core functionality works without internet (Phase 2)

### Target Users
- **Primary**: Field service technicians
- **Secondary**: Maintenance personnel, installation teams
- **Environment**: Outdoor conditions, wearing gloves, time-sensitive situations
- **Devices**: iOS and Android smartphones (375px - 428px width)

---

## Brand Identity

### Color Palette

**Primary - Dark Emerald Green (#095C53)**
- Usage: Headers, navigation, primary CTAs, brand elements
- Represents: Reliability, professionalism, industrial strength
- Accessibility: WCAG AA compliant with white text

**Secondary - Golden Yellow (#FEC951)**
- Usage: Action buttons, highlights, success states
- Represents: Solutions, illumination, positivity
- Accessibility: High contrast, attention-grabbing

**Tertiary - Teal Blue/Cyan (#2BB6C1)**
- Usage: Links, active states, information highlights
- Represents: Technology, trust, communication
- Accessibility: Works well with both light and dark backgrounds

**Neutral - Gray (#666666 and variations)**
- Light Gray: #F8F9FA (backgrounds)
- Medium Gray: #666666 (body text)
- Dark Gray: #333333 (headings)
- Border Gray: #E0E0E0

### Typography
- **Primary Font**: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif
- **Rationale**: Native system fonts for optimal performance and familiarity
- **Sizes**: 
  - H1: 28-36px (page titles)
  - H2: 20-24px (section headers)
  - Body: 15-16px (readable on mobile)
  - Small: 12-14px (metadata, timestamps)

---

## Screen-by-Screen Breakdown

### 1. Login Screen
**File**: `mobile-01-login.html`

**Purpose**: Secure authentication gateway

**Key Elements**:
- Utilyst logo prominently displayed
- Welcome message ("Welcome Back")
- Employee ID input field
- Password input field
- "Forgot Password?" link
- Primary "Sign In" button (Golden Yellow)
- SSO alternative option

**Design Decisions**:
- Gradient background using primary colors for brand immersion
- White form card with ample padding for focus
- Large, tappable buttons (minimum 44px height)
- Clear visual hierarchy: logo → greeting → form → action

**User Flow**:
```
Launch App → Login Screen
    ├─→ Enter credentials → Dashboard
    ├─→ Forgot password → Password recovery
    └─→ SSO → External authentication → Dashboard
```

**Technical Considerations**:
- Secure credential storage
- Biometric authentication (Touch ID/Face ID) - Phase 2
- Remember me functionality
- Session timeout handling

---

### 2. Home Dashboard
**File**: `mobile-02-home.html`

**Purpose**: Central hub for quick access and session overview

**Key Elements**:
- **Header Section** (Dark Emerald Green):
  - Utilyst logo
  - Profile icon
  - Personalized greeting ("Good Morning, John")
  - Motivational subtitle

- **Quick Actions** (3 primary actions):
  - 💬 Start New Issue
  - 📷 Scan Equipment
  - 🔍 Browse Manuals

- **Recent Sessions**:
  - Session cards with status indicators
  - Timestamp and equipment info
  - Resolution status badges

- **Bottom Navigation**:
  - 🏠 Home (active)
  - 📋 History
  - 📚 Manuals
  - ⚙️ Settings

**Design Decisions**:
- Quick actions use icon + text for clarity
- Recent sessions with color-coded status (green for resolved)
- Persistent bottom navigation for easy app navigation
- Card-based layout with shadows for depth

**User Flow**:
```
Dashboard
    ├─→ Start New Issue → Issue Input Screen
    ├─→ Scan Equipment → Camera Screen
    ├─→ Browse Manuals → Manual Library
    ├─→ Recent Session → Session Detail
    └─→ Bottom Nav → Other sections
```

---

### 3. New Issue Input Screen
**File**: `mobile-03-new-issue.html`

**Purpose**: Capture comprehensive issue information

**Key Elements**:
- Back button (top left)
- **Equipment Selector** (grid layout):
  - Visual equipment cards
  - Selected state (Teal border + background)
  - Icons for quick identification

- **Text Input Area**:
  - Large textarea for issue description
  - Placeholder guidance
  - Example pre-filled for demo

- **Media Options**:
  - 📷 Camera
  - 🖼️ Gallery
  - 🎤 Voice (for hands-free input)

- **Quick Suggestions**:
  - Common issue chips
  - One-tap population of frequent problems

- **Submit Button** (Golden Yellow):
  - "Get Help →" with arrow
  - Fixed at bottom for thumb reach

**Design Decisions**:
- Equipment selector first to establish context
- Large touch targets for glove-friendly use
- Media options as visual buttons (not hidden menu)
- Suggestions reduce typing for common scenarios
- Sticky submit button always accessible

**User Flow**:
```
New Issue Screen
    ├─→ Select equipment type
    ├─→ Describe issue (text/voice)
    ├─→ Optional: Add photos/video
    ├─→ Optional: Select suggestion chip
    └─→ Submit → AI Chat Screen
```

---

### 4. AI Chat Interface
**File**: `mobile-04-chat.html`

**Purpose**: Interactive troubleshooting conversation

**Key Elements**:
- **Header** (Dark Emerald Green):
  - Back button
  - AI Assistant avatar (🤖)
  - Status indicator (● Online)

- **Chat Messages**:
  - User messages (Teal, right-aligned)
  - AI messages (White, left-aligned)
  - Timestamps
  - Avatar icons for visual distinction

- **Step Cards** (within AI messages):
  - Numbered steps
  - Color-coded borders (Teal)
  - Clear instructions
  - Action buttons (✓ Done, 📷 Take Photo)

- **Typing Indicator**:
  - Animated dots for AI thinking state

- **Input Bar** (bottom):
  - 📎 Attachment button
  - Text input field
  - → Send button (Golden Yellow)

**Design Decisions**:
- Familiar chat interface pattern (WhatsApp-like)
- Step cards visually distinct from regular messages
- Action buttons embedded for quick responses
- Typing indicator manages expectations
- Input bar always accessible but not intrusive

**User Flow**:
```
Chat Interface
    ├─→ View AI guidance
    ├─→ Mark step complete
    ├─→ Take photo → Camera Screen → Return with image
    ├─→ Ask follow-up question
    ├─→ Continue conversation
    └─→ Issue resolved → Success Screen
```

**Advanced Features** (Phase 2):
- Voice input/output
- Image annotation
- Video support
- Screen sharing

---

### 5. Camera Capture Screen
**File**: `mobile-05-camera.html`

**Purpose**: Capture high-quality equipment photos

**Key Elements**:
- **Full-screen camera view**:
  - Live camera feed
  - Focus frame with corner indicators (Golden Yellow)
  - Placeholder shown in mockup

- **Top Controls**:
  - ✕ Close/Cancel
  - ⚡ Flash toggle

- **Hint Banner** (bottom, Golden Yellow):
  - 💡 Icon
  - Quick Tip title
  - Helpful guidance text

- **Bottom Controls**:
  - 🖼️ Gallery access
  - ⭕ Capture button (large, white)
  - 🔄 Flip camera

**Design Decisions**:
- Full-screen for maximum viewfinder
- Large capture button for easy tapping
- Focus frame guides user to center subject
- Contextual hints reduce errors
- Minimal UI to avoid distraction

**User Flow**:
```
Camera Screen
    ├─→ Adjust position/angle
    ├─→ Tap capture → Preview
    ├─→ Confirm → Return to chat with image
    ├─→ Retake → Capture again
    └─→ Cancel → Return without image
```

**Technical Considerations**:
- Auto-focus on tap
- Image compression for upload
- Metadata capture (location, timestamp)
- Offline queueing if no connection

---

### 6. Issue Resolved Screen
**File**: `mobile-06-resolved.html`

**Purpose**: Confirm success and collect feedback

**Key Elements**:
- **Success Animation**:
  - ✓ checkmark in Teal circle
  - Subtle animation (CSS)

- **Success Message**:
  - Bold headline "Issue Resolved!"
  - Detailed confirmation message

- **Session Summary Card**:
  - 📋 Icon header
  - Key metrics table:
    - Issue Type
    - Equipment
    - Error Code
    - Resolution Time
    - Steps Completed

- **Action Buttons**:
  - 📄 View Full Report (Golden Yellow)
  - 🏠 Back to Home (outlined)

- **Rating Section** (bottom):
  - "How helpful was this session?"
  - ⭐⭐⭐⭐⭐ star rating

**Design Decisions**:
- Celebratory design reinforces success
- Summary provides reference for documentation
- Report generation for records/compliance
- Rating collection for system improvement
- Clear path back to home or next session

**User Flow**:
```
Resolved Screen
    ├─→ View report → PDF/Email
    ├─→ Rate session → Thank you message
    └─→ Back to Home → Dashboard
```

---

## User Journey Map

### Complete Flow: Issue to Resolution

```
1. LOGIN
   └─→ Dashboard

2. DASHBOARD
   ├─→ Start New Issue
   │   └─→ New Issue Screen
   │       ├─→ Select equipment
   │       ├─→ Describe issue
   │       ├─→ Add photo (optional)
   │       └─→ Submit
   │           └─→ AI Chat
   └─→ Or: Scan Equipment
       └─→ Camera Screen
           └─→ Capture
               └─→ AI Chat (with image analysis)

3. AI CHAT
   ├─→ Receive guidance
   ├─→ Follow steps
   ├─→ Take verification photos
   └─→ Confirm resolution
       └─→ Resolved Screen

4. RESOLVED
   ├─→ View report
   ├─→ Rate session
   └─→ Back to Dashboard
```

### Average Session Duration
- Simple issues: 5-10 minutes
- Complex issues: 15-30 minutes
- Installation guidance: 20-45 minutes

---

## Responsive Design Specifications

### Breakpoints
- **Mobile Small**: 320px - 374px (iPhone SE)
- **Mobile Medium**: 375px - 413px (iPhone 12/13/14)
- **Mobile Large**: 414px - 428px (iPhone Pro Max)

### Touch Targets
- **Minimum size**: 44px × 44px (iOS guideline)
- **Recommended**: 48px × 48px (Android guideline)
- **Spacing**: 8px minimum between tappable elements

### Font Scaling
- Support iOS Dynamic Type
- Support Android font size preferences
- Test at 200% zoom for accessibility

---

## Accessibility Features

### Current Implementation
✅ High contrast color combinations (WCAG AA)
✅ Large, readable fonts (minimum 15px body text)
✅ Clear visual hierarchy
✅ Descriptive button labels
✅ Adequate touch target sizes

### Phase 2 Enhancements
- Screen reader optimization
- Voice control integration
- Dark mode support
- Reduced motion option
- Haptic feedback

---

## Technical Stack

### Frontend Framework
- **Option 1**: React Native (cross-platform)
- **Option 2**: Flutter (cross-platform)
- **Option 3**: Native iOS (Swift) + Native Android (Kotlin)

**Recommendation**: React Native for:
- Code reuse with web
- Faster development
- Large ecosystem
- Good performance

### State Management
- Redux Toolkit or Zustand
- Persistent storage with AsyncStorage

### API Integration
- Axios for HTTP requests
- WebSocket for real-time chat
- Retry logic for offline scenarios

### Media Handling
- react-native-camera or expo-camera
- Image compression before upload
- Local caching of media

### Authentication
- JWT tokens
- Biometric authentication (TouchID/FaceID)
- SSO integration (OAuth 2.0)

---

## Performance Targets

### Key Metrics
- **App Launch**: < 2 seconds
- **Screen Transitions**: < 300ms
- **API Response**: < 500ms average
- **Image Upload**: < 3 seconds
- **Chat Message**: < 100ms latency

### Optimization Strategies
- Lazy loading for screens
- Image optimization and caching
- Debounced search inputs
- Virtualized lists for history
- Preloading critical data

---

## Testing Strategy

### Manual Testing
- All user flows end-to-end
- Accessibility with VoiceOver/TalkBack
- Various device sizes
- Different network conditions
- Edge cases (empty states, errors)

### Automated Testing
- Unit tests for business logic
- Integration tests for API calls
- E2E tests with Detox or Appium
- Visual regression testing

### Beta Testing
- Internal team (50 users)
- Select customers (100 users)
- Feedback collection via in-app surveys

---

## Deployment Plan

### Phase 1: MVP (Months 1-2)
✅ Screens 1-6 (all mockups)
✅ Text and image input
✅ Basic chat interface
✅ Session history
✅ Manual browsing

### Phase 2: Enhancement (Months 3-4)
- Voice input/output
- Video support
- Offline mode
- Dark mode
- Advanced analytics

### Phase 3: Scale (Months 5-6)
- Multi-language support
- AR overlays
- Predictive maintenance
- Integration with equipment sensors

---

## Files Included

1. **mobile-01-login.html** - Login screen
2. **mobile-02-home.html** - Dashboard
3. **mobile-03-new-issue.html** - Issue input
4. **mobile-04-chat.html** - AI chat interface
5. **mobile-05-camera.html** - Camera capture
6. **mobile-06-resolved.html** - Success screen
7. **mobile-mockup-showcase.html** - Complete overview

---

## Next Steps

1. **Design Review**: Stakeholder feedback on mockups
2. **User Testing**: Validate with 5-10 technicians
3. **Development**: Begin React Native implementation
4. **Backend Integration**: Connect to FastAPI server
5. **Beta Release**: Limited rollout to pilot group
6. **Iteration**: Refine based on real-world usage

---

**Last Updated**: October 25, 2025
**Version**: 1.0
**Status**: Mockup Complete, Ready for Development

# CrewAI AMP Deployment Guide

Complete guide for deploying CrewSight-AI to CrewAI AMP platform.

© 2025 Utilyst Inc. All rights reserved.

## 📋 Prerequisites

- ✅ CrewAI account (free tier available)
- ✅ GitHub repository with CrewSight-AI
- ✅ OpenAI API key
- ✅ Anthropic API key
- ✅ CrewAI CLI installed

## 🚀 Quick Deployment (3 Steps)

### Step 1: Install CrewAI CLI

```bash
pip install crewai
```

### Step 2: Login to CrewAI

```bash
crewai login
```

Follow the prompts to authenticate with your CrewAI account.

### Step 3: Deploy

```bash
cd crewsight-ai
crewai deploy create
```

That's it! Your crew will be deployed to CrewAI AMP.

## 📁 Required Project Structure

CrewAI AMP expects this structure (✅ already configured):

```
crewsight-ai/
├── src/crewsight/
│   ├── main.py              ✅ Entry point
│   ├── crew.py              ✅ Crew definition
│   ├── config/
│   │   ├── agents.yaml      ✅ Agent configs
│   │   └── tasks.yaml       ✅ Task configs
│   └── tools/               ✅ Custom tools
├── pyproject.toml           ✅ Project metadata
└── requirements.txt         ✅ Dependencies
```

## ⚙️ Environment Variables

Configure in CrewAI AMP dashboard:

```env
OPENAI_API_KEY=your-key-here
ANTHROPIC_API_KEY=your-key-here
SERPER_API_KEY=your-key-here (optional)
```

## 🔗 Deployment Commands

### Create New Deployment

```bash
crewai deploy create
```

### Update Existing Deployment

```bash
crewai deploy push
```

### Check Deployment Status

```bash
crewai deploy status
```

### View Deployment Logs

```bash
crewai deploy logs
```

### Delete Deployment

```bash
crewai deploy delete
```

## 🌐 CrewAI AMP Endpoints

After deployment, CrewAI AMP provides these endpoints:

### Kickoff a Crew Run

```bash
POST https://api.crewai.com/v1/crews/{crew_id}/kickoff

Headers:
  Authorization: Bearer YOUR_API_KEY
  Content-Type: application/json

Body:
{
  "inputs": {
    "google_drive_url": "https://drive.google.com/drive/folders/...",
    "document_type": "research_papers",
    "analysis_focus": "key_findings",
    "output_format": "summary"
  }
}
```

### Check Run Status

```bash
GET https://api.crewai.com/v1/crews/{crew_id}/runs/{run_id}
```

### Get Run Results

```bash
GET https://api.crewai.com/v1/crews/{crew_id}/runs/{run_id}/result
```

## 📱 Mobile App Integration

The mobile app connects to CrewAI AMP via REST API:

```javascript
// Mobile app example
const response = await fetch(
  'https://api.crewai.com/v1/crews/{crew_id}/kickoff',
  {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      inputs: {
        google_drive_url: driveUrl,
        document_type: 'field_reports',
        analysis_focus: 'troubleshooting_steps'
      }
    })
  }
);

const runId = response.data.run_id;

// Poll for results
const checkStatus = async () => {
  const statusResponse = await fetch(
    `https://api.crewai.com/v1/crews/{crew_id}/runs/${runId}`
  );
  
  if (statusResponse.data.status === 'completed') {
    // Show results in mobile app
    displayResults(statusResponse.data.result);
  }
};
```

## 🔧 Troubleshooting

### Build Failed

**Issue**: Deployment build fails

**Solution**:
```bash
# Check project structure
ls -la src/crewsight/

# Verify dependencies
pip install -r requirements.txt

# Check pyproject.toml is valid
cat pyproject.toml
```

### Agent Errors

**Issue**: Agents not working correctly

**Solution**:
- Verify `config/agents.yaml` syntax
- Check API keys are set correctly
- Review agent configurations

### Tool Errors

**Issue**: Custom tools not found

**Solution**:
```bash
# Ensure tools are properly imported
cat src/crewsight/tools/__init__.py

# Check tool class inherits from BaseTool
cat src/crewsight/tools/public_google_drive_processor.py
```

## 📊 Monitoring & Logs

### View Real-time Logs

```bash
crewai deploy logs --follow
```

### Check Metrics

Access CrewAI AMP dashboard:
- Execution times
- Success rates
- API usage
- Error rates

## 💰 Pricing Tiers

### Free Tier
- ✅ 100 crew runs/month
- ✅ Basic monitoring
- ✅ Community support

### Pro Tier
- ✅ Unlimited crew runs
- ✅ Advanced monitoring
- ✅ Priority support
- ✅ Custom domains

Contact: john@utilyst.com for enterprise pricing

## 🔐 Security

### API Keys

- Never commit API keys to repository
- Use CrewAI AMP environment variables
- Rotate keys regularly

### Access Control

- Set up team permissions in dashboard
- Use separate keys for dev/staging/prod
- Enable audit logging

## 📚 Additional Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [Deployment Guide](https://docs.crewai.com/en/enterprise/guides/deploy-crew)
- [API Reference](https://docs.crewai.com/api-reference)
- [CrewAI Discord](https://discord.gg/crewai)

## ✅ Deployment Checklist

Before deploying to CrewAI AMP:

- [ ] Project structure follows CrewAI conventions
- [ ] `pyproject.toml` is properly configured
- [ ] All dependencies listed in `requirements.txt`
- [ ] Agents defined in `config/agents.yaml`
- [ ] Tasks defined in `config/tasks.yaml`
- [ ] Custom tools properly imported
- [ ] API keys ready for environment variables
- [ ] Local testing completed successfully
- [ ] CrewAI CLI installed and authenticated
- [ ] GitHub repository is up to date

## 🎯 For Agentic AI Challenge

**Submission Requirements**:
- ✅ Deployed to CrewAI AMP (free tier OK)
- ✅ GitHub repository shared
- ✅ Project accessible via CrewAI AMP URL
- ✅ Deadline: October 31st, 2025
- ✅ Winners announced: November 20th at CrewAI Signal 2025

**Deployment Command**:
```bash
crewai deploy create
```

**Share with CrewAI**:
- GitHub URL: https://github.com/Utilyst-public/CrewSight-AI
- CrewAI AMP URL: (provided after deployment)
- Demo video: (optional but recommended)

## 🎬 Demo Video Tips

If creating a demo video:
1. Show the problem CrewSight-AI solves
2. Demonstrate mobile app mockups
3. Run a live document processing workflow
4. Show the final report output
5. Highlight multi-agent collaboration
6. Mention Utilyst Inc. use case

## 📞 Support

For deployment issues:
- CrewAI Discord: https://discord.gg/crewai
- CrewAI Docs: https://docs.crewai.com/
- Email: john@utilyst.com (Utilyst Inc.)

---

© 2025 Utilyst Inc. All rights reserved.

**Ready to deploy!** 🚀

```bash
crewai deploy create
```

# Contributing to Bangladesh Laws Documentation

Thank you for your interest in contributing to this project! This guide will help you understand how to contribute effectively.

## 🎯 Ways to Contribute

### 1. Content Contributions
- **Add missing acts**: Help complete volumes with missing legislation
- **Fix errors**: Correct typos, formatting issues, or content errors
- **Improve formatting**: Enhance readability and document structure
- **Add translations**: Help with Bangla-English translations

### 2. Technical Contributions
- **Website improvements**: Enhance the MkDocs site functionality
- **Documentation**: Improve project documentation
- **Bug fixes**: Resolve technical issues

### 3. Quality Assurance
- **Verify content**: Cross-check with official government sources
- **Test functionality**: Ensure website features work correctly
- **Report issues**: Identify and document problems

## 🚀 Getting Started

### Prerequisites
- Git installed on your computer
- Python 3.7+ and pip
- Basic knowledge of Markdown
- Familiarity with the structure of legal documents

### Setup Development Environment

1. **Fork the repository**
   - Go to the [project repository](https://github.com/lawsofbangladesh/lawsofbangladesh.github.io)
   - Click "Fork" to create your own copy

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/lawsofbangladesh.github.io.git
   cd lawsofbangladesh.github.io
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start development server**
   ```bash
   mkdocs serve
   ```

5. **View the site**
   Open `http://127.0.0.1:8000` in your browser

## 📝 Content Guidelines

### Adding New Acts

1. **Verify the source**: Always check the official government website first
2. **Follow naming convention**: Use `act-details-XXXX.md` format
3. **Use consistent structure**:
   ```markdown
   # The Act Name, Year
   
   **Act No:** XX  
   **Year:** YYYY  
   
   ## Preamble
   [Act preamble/introduction]
   
   ## Sections
   
   ### Section 1 - Title
   [Section content]
   
   ### Section 2 - Next section
   [Section content]
   
   ---
   
   *Brief summary or note about the act*
   ```

### Formatting Standards

- **Headers**: Use proper Markdown hierarchy (# ## ### ####)
- **Bold text**: Use `**text**` for act numbers, years, important terms
- **Lists**: Use `-` or `*` for unordered lists, `1.` for ordered lists
- **Links**: Use descriptive link text, not "click here"
- **Bangla text**: Ensure proper Unicode encoding

### Content Verification

Before submitting content:

1. ✅ **Check official source**: Verify against [bdlaws.minlaw.gov.bd](http://bdlaws.minlaw.gov.bd/)
2. ✅ **Spell check**: Review for typos and grammar
3. ✅ **Format check**: Ensure consistent formatting
4. ✅ **Link check**: Verify all links work correctly

## 🔄 Submission Process

### For Content Changes

1. **Create a feature branch**
   ```bash
   git checkout -b add-act-XXXX
   # or
   git checkout -b fix-typo-volume-X
   ```

2. **Make your changes**
   - Edit existing files or create new ones
   - Follow the formatting guidelines
   - Test your changes locally

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: The New Act Name, Year (Act XXXX)"
   # or
   git commit -m "Fix: Typo in Volume X Act Y"
   ```

4. **Push to your fork**
   ```bash
   git push origin add-act-XXXX
   ```

5. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Provide a clear description of your changes
   - Reference any related issues

### Pull Request Guidelines

**Title Format:**
- `Add: The Act Name, Year (Act XXXX)`
- `Fix: Description of what was fixed`
- `Update: Description of what was updated`

**Description should include:**
- What changes were made
- Why the changes were necessary
- Source verification (link to official government page)
- Any testing performed

**Example:**
```
## Changes Made
- Added The Example Act, 2023 (Act XXXX) to Volume XX
- Fixed formatting in Section 3 of the act
- Added proper cross-references

## Source Verification
Verified against: http://bdlaws.minlaw.gov.bd/act-details-XXXX.php

## Testing
- [x] Content displays correctly in development server
- [x] All links work properly
- [x] Formatting is consistent with other acts
```

## 🐛 Reporting Issues

### Before Reporting
1. Check if the issue already exists
2. Verify the problem against official sources
3. Test in multiple browsers if it's a website issue

### Issue Categories
- **Content Error**: Wrong information, typos, formatting issues
- **Missing Content**: Acts or sections that should be included
- **Technical Bug**: Website functionality problems
- **Enhancement**: Suggestions for improvements

### Issue Template
```
**Issue Type:** [Content Error/Missing Content/Technical Bug/Enhancement]

**Description:**
Clear description of the issue

**Steps to Reproduce:** (for bugs)
1. Go to...
2. Click on...
3. See error...

**Expected Behavior:**
What should happen

**Current Behavior:**
What actually happens

**Source Verification:**
Link to official government source (if applicable)

**Browser/Device:** (for technical issues)
Browser version and operating system
```

## 📚 Style Guide

### Markdown Best Practices
- Use consistent heading levels
- Leave blank lines around headers
- Use emphasis sparingly and consistently
- Keep line lengths reasonable (80-100 characters)

### Legal Document Conventions
- Capitalize act names properly
- Use consistent section numbering
- Include act numbers and years
- Maintain original legal language where possible

### Bangla Text Guidelines
- Use proper Unicode encoding
- Maintain consistency in transliteration
- Include both Bangla and English where helpful

## 🤝 Code of Conduct

### Our Standards
- **Respectful communication**: Be kind and respectful to all contributors
- **Constructive feedback**: Provide helpful, actionable feedback
- **Collaborative spirit**: Work together toward common goals
- **Quality focus**: Prioritize accuracy and usefulness

### Unacceptable Behavior
- Personal attacks or discriminatory language
- Harassment of any kind
- Spam or irrelevant contributions
- Deliberate misinformation

## 🏆 Recognition

Contributors will be recognized in several ways:
- Listed in project documentation
- GitHub contributor statistics
- Special mentions for significant contributions
- Community appreciation

## ❓ Questions and Help

### Getting Help
- **GitHub Discussions**: For general questions and discussions
- **GitHub Issues**: For specific problems or bugs
- **Documentation**: Check existing documentation first

### Mentorship
New contributors are welcome! Don't hesitate to ask for help:
- Start with small contributions
- Ask questions if you're unsure
- Review existing contributions for examples

## 📋 Checklist for Contributors

Before submitting:

- [ ] Changes are verified against official sources
- [ ] Formatting follows project guidelines
- [ ] All links work correctly
- [ ] Content is properly spelled and grammatically correct
- [ ] Commit messages are clear and descriptive
- [ ] Pull request includes proper description
- [ ] Local testing has been performed

---

Thank you for contributing to making Bangladesh's laws more accessible! 🇧🇩

*For questions about this contributing guide, please open an issue or discussion.*

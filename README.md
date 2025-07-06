# Bangladesh Laws Documentation 🇧🇩

[![Website](https://img.shields.io/website?url=https%3A//bangladeshlaw.github.io)](https://bangladeshlaw.github.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MkDocs](https://img.shields.io/badge/Built%20with-MkDocs-blue)](https://www.mkdocs.org/)

A comprehensive, searchable, and accessible digital archive of Bangladesh laws, sourced from the official Government of Bangladesh website.

## 🎯 Purpose

This project aims to make Bangladesh's legal framework more accessible to citizens, lawyers, researchers, and anyone interested in understanding the country's laws. By providing a modern, searchable interface, we hope to democratize access to legal information.

## 🌐 Live Website

Visit the live documentation at: **[bangladeshlaw.github.io](https://bangladeshlaw.github.io)**

## 📚 Content

The documentation includes:

- **56 Volumes** of laws covering different time periods
- **Historical laws** from 1799 to present
- **Complete acts** with full text and sections
- **Chronological organization** by volumes
- **Search functionality** across all documents
- **Responsive design** for mobile and desktop

### Volume Coverage

- **Volume 1**: Regulation V of 1799 to Act No. I of 1872 (Colonial foundation)
- **Volume 2**: Act No. III of 1872 to Act No. II of 1882 (Commercial law establishment)
- **Volumes 3-56**: Continuing chronological coverage to present day

## 🚀 Features

- ✅ **Fast Search**: Instant search across all legal documents
- ✅ **Mobile Responsive**: Works perfectly on all devices
- ✅ **Dark/Light Mode**: Automatic theme switching
- ✅ **Bangla Support**: Full Unicode Bangla text support
- ✅ **Navigation**: Easy browsing with table of contents
- ✅ **Offline Ready**: Can be used without internet connection
- ✅ **Print Friendly**: Clean printing support

## 🛠️ Technology Stack

- **[MkDocs](https://www.mkdocs.org/)**: Static site generator
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)**: Modern theme
- **[GitHub Pages](https://pages.github.com/)**: Free hosting
- **[Python](https://www.python.org/)**: Backend processing scripts

## 🏗️ Project Structure

```
lawsofbangladesh.github.io/
├── docs/
│   ├── index.md                 # Homepage
│   ├── assets/                  # Images and icons
│   └── laws/
│       ├── index.md            # Laws overview
│       ├── volume-1/           # Volume 1 acts
│       │   ├── index.md
│       │   └── act-details-*.md
│       ├── volume-2/           # Volume 2 acts
│       └── ...                 # Other volumes
├── scripts/                    # Automation scripts
├── mkdocs.yml                  # Site configuration
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lawsofbangladesh/lawsofbangladesh.github.io.git
   cd lawsofbangladesh.github.io
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server**
   ```bash
   mkdocs serve
   ```

4. **View the site**
   Open your browser and go to `http://127.0.0.1:8000`

### Building for Production

```bash
mkdocs build
```

This creates a `site/` directory with static files ready for deployment.

## 📖 Usage

### Browsing Laws

1. Visit the [live website](https://bangladeshlaw.github.io)
2. Use the navigation menu to browse by volume
3. Use the search bar to find specific acts or keywords
4. Click on any act title to view its full content

### Searching

- **Global Search**: Use the search bar in the header
- **Volume Search**: Browse within specific volumes
- **Keyword Search**: Search for specific terms across all documents

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Content Contributions

1. **Report Errors**: Found a typo or formatting issue? Open an issue
2. **Add Missing Acts**: Help us complete missing legislation
3. **Improve Formatting**: Enhance readability and structure
4. **Translations**: Help with English translations of Bangla acts

### Technical Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test your changes**
   ```bash
   mkdocs serve
   ```
5. **Commit and push**
   ```bash
   git commit -m "Description of changes"
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**

### Guidelines

- Maintain consistent formatting across documents
- Verify content accuracy against official sources
- Test changes before submitting
- Write clear commit messages
- Update documentation when needed

## 📋 Data Sources

All content is sourced from the **official Government of Bangladesh website**:

- **Primary Source**: [bdlaws.minlaw.gov.bd](http://bdlaws.minlaw.gov.bd/)
- **Authority**: Legislative and Parliamentary Affairs Division
- **Ministry**: Ministry of Law, Justice and Parliamentary Affairs

### Content Verification

When contributing or using this content:

1. ✅ **Always verify** against the official government website
2. ✅ **Check for updates** regularly as laws may be amended
3. ✅ **Cross-reference** with official publications
4. ❌ **Do not rely solely** on this unofficial mirror for legal decisions

## ⚖️ Legal Disclaimer

**IMPORTANT**: This is an **unofficial mirror** of government legal documents.

- 📋 **For Official Use**: Always refer to [bdlaws.minlaw.gov.bd](http://bdlaws.minlaw.gov.bd/)
- ⚖️ **Legal Advice**: This site does not provide legal advice
- 📅 **Currency**: Laws may have been updated since last sync
- 🔍 **Verification**: Always verify content with official sources
- 📞 **Questions**: Contact relevant government authorities for clarifications

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What this means:

- ✅ **Free to use** for any purpose
- ✅ **Modify and distribute** freely
- ✅ **Commercial use** allowed
- ✅ **Private use** allowed
- ❗ **Attribution required** (keep license notice)
- ❗ **No warranty** provided

### Government Content

The legal texts themselves are **public domain** government documents. Our license applies to:
- The compilation and organization
- The website structure and code
- Documentation and scripts

## 🔧 Maintenance

### Automated Updates

- Scripts in `/scripts/` directory help automate content updates
- Regular synchronization with government website
- Automated formatting and validation

### Manual Updates

Contributors can manually add new acts or update existing ones following the established format.

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/lawsofbangladesh/lawsofbangladesh.github.io/issues)
- **Discussions**: [GitHub Discussions](https://github.com/lawsofbangladesh/lawsofbangladesh.github.io/discussions)
- **Email**: Contact through GitHub profile

## 🙏 Acknowledgments

- **Government of Bangladesh** for making laws publicly available
- **Legislative and Parliamentary Affairs Division** for maintaining the official database
- **MkDocs Material** team for the excellent documentation theme
- **Contributors** who help maintain and improve this project

## 📊 Project Stats

- **Total Volumes**: 56
- **Acts Covered**: 1000+ individual acts
- **Time Span**: 1799 to present
- **Languages**: English and Bangla
- **File Format**: Markdown for easy editing

---

**🇧🇩 Made for the people of Bangladesh with ❤️**

*This project is not affiliated with the Government of Bangladesh. It is an independent initiative to improve access to legal information.*

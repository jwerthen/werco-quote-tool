# QuoteEngine - Manufacturing Quote Automation Tool

## Product Specification Document

**Version:** 1.0  
**Author:** Werco Manufacturing  
**Date:** January 2026  
**Status:** Development Specification

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement](#2-problem-statement)
3. [Product Vision](#3-product-vision)
4. [Technical Architecture](#4-technical-architecture)
5. [File Parsing Specifications](#5-file-parsing-specifications)
6. [Feature Extraction Engine](#6-feature-extraction-engine)
7. [Process Routing Engine](#7-process-routing-engine)
8. [Cost Calculation Engine](#8-cost-calculation-engine)
9. [Data Models](#9-data-models)
10. [API Specifications](#10-api-specifications)
11. [User Interface Requirements](#11-user-interface-requirements)
12. [Output Generation](#12-output-generation)
13. [Accuracy & Validation](#13-accuracy--validation)
14. [Development Phases](#14-development-phases)
15. [Technology Stack](#15-technology-stack)
16. [Testing Requirements](#16-testing-requirements)

---

## 1. Executive Summary

QuoteEngine is an AI-powered manufacturing quote automation tool designed for metal fabrication shops. The system ingests CAD files (STEP, DXF) and technical drawings (PDF), extracts geometry and manufacturing features, suggests process routing, calculates costs, and generates professional quote documents.

### Key Capabilities

- **Automated geometry extraction** from STEP and DXF files
- **Intelligent process routing** based on part characteristics
- **Accurate cost calculation** with material, labor, and consumables
- **Professional document generation** for internal review and customer quotes
- **Full traceability** of how quotes were built

### Target Users

- Estimators at metal fabrication shops
- Shop managers reviewing quotes
- Sales teams preparing customer quotes
- Operations teams planning production

---

## 2. Problem Statement

### Current Pain Points

1. **Manual Measurement** - Estimators spend 2-4 hours per quote manually measuring drawings and calculating material needs

2. **No Geometry Extraction** - STEP/DXF files contain rich geometry data that is never systematically extracted

3. **Tribal Knowledge** - Process routing expertise lives in estimators' heads, not in systems

4. **Inconsistent Quoting** - Different estimators produce different quotes for the same part

5. **No Audit Trail** - No visibility into how a quote was calculated

6. **Slow Turnaround** - Complex quotes take days, causing lost opportunities

### Business Impact

- Lost quotes due to slow response time
- Margin erosion from inaccurate estimates
- Knowledge loss when experienced estimators leave
- Inability to scale quoting capacity

---

## 3. Product Vision

### Core Principle

> "Every quote should be defensible, traceable, and consistent - built from actual geometry, not guesswork."

### Product Goals

1. **Reduce quote time by 75%** - From 2-4 hours to 30 minutes for complex jobs
2. **Improve accuracy to ±10%** - Quoted hours vs actual hours
3. **100% traceability** - Every line item traceable to geometry and routing logic
4. **Consistency** - Same part = same quote, regardless of estimator
5. **Knowledge capture** - Institutional knowledge encoded in routing rules

### Differentiators

- **Transparent logic** - Users see exactly how the quote was built
- **Structural/weldment focus** - Purpose-built for fabrication, not just sheet metal
- **Hybrid AI + rules** - Combines AI extraction with configurable business rules
- **Shop-floor validated** - Built by fabricators, for fabricators

---

## 4. Technical Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                                 │
│    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐        │
│    │   Web App    │    │  Mobile App  │    │   CLI Tool   │        │
│    │   (React)    │    │   (Future)   │    │   (Python)   │        │
│    └──────────────┘    └──────────────┘    └──────────────┘        │
└─────────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                          API LAYER                                   │
│                    FastAPI / Python Backend                          │
│    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐        │
│    │  /api/files  │    │ /api/quotes  │    │  /api/parts  │        │
│    └──────────────┘    └──────────────┘    └──────────────┘        │
└─────────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       PROCESSING LAYER                               │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │
│  │  File Parser    │  │    Feature      │  │    Process      │     │
│  │    Engine       │  │   Extraction    │  │    Routing      │     │
│  │                 │  │    Engine       │  │    Engine       │     │
│  │ • STEP Parser   │  │                 │  │                 │     │
│  │ • DXF Parser    │  │ • Geometry      │  │ • Rule Engine   │     │
│  │ • PDF Parser    │  │ • Features      │  │ • Time Calc     │     │
│  │                 │  │ • Complexity    │  │ • Sequencing    │     │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘     │
│                                                                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │
│  │     Cost        │  │    Document     │  │    Similar      │     │
│  │  Calculation    │  │   Generation    │  │     Part        │     │
│  │    Engine       │  │    Engine       │  │    Matching     │     │
│  │                 │  │                 │  │                 │     │
│  │ • Material      │  │ • DOCX/PDF     │  │ • Vector DB     │     │
│  │ • Labor         │  │ • Excel        │  │ • Similarity    │     │
│  │ • Consumables   │  │ • Travelers    │  │ • History       │     │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘     │
└─────────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        DATA LAYER                                    │
│    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐        │
│    │  PostgreSQL  │    │    Redis     │    │ File Storage │        │
│    │  (Primary)   │    │   (Cache)    │    │  (S3/Local)  │        │
│    └──────────────┘    └──────────────┘    └──────────────┘        │
└─────────────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| File Parser Engine | Ingest and parse STEP, DXF, PDF files |
| Feature Extraction Engine | Extract geometry, holes, features, complexity |
| Process Routing Engine | Determine operations, sequence, and time estimates |
| Cost Calculation Engine | Calculate material, labor, consumables, margin |
| Document Generation Engine | Create quotes, travelers, reports |
| Similar Part Matching | Find historical quotes for similar geometry |

---

## 5. File Parsing Specifications

### 5.1 STEP File Parser

#### Supported Formats
- STEP AP203 (Configuration Controlled 3D Design)
- STEP AP214 (Automotive Design)
- STEP AP242 (Managed Model-based 3D Engineering)

#### Required Libraries
```python
# Primary: OpenCASCADE via PythonOCC
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.BRepGProp import brepgprop_VolumeProperties
from OCC.Core.GProp import GProp_GProps

# Fallback: FreeCAD
import FreeCAD
import Part
```

#### Extraction Requirements

```python
class STEPExtractor:
    """
    Extract geometry and features from STEP files.
    """
    
    def extract(self, filepath: str) -> STEPExtractionResult:
        """
        Main extraction method.
        
        Returns:
            STEPExtractionResult with all extracted data
        """
        pass
    
    def get_bounding_box(self) -> BoundingBox:
        """
        Extract bounding box dimensions.
        
        Returns:
            BoundingBox(x_min, x_max, y_min, y_max, z_min, z_max, 
                        length, width, height, units)
        """
        pass
    
    def get_volume(self) -> float:
        """
        Calculate solid volume in cubic inches.
        Used for weight estimation.
        """
        pass
    
    def get_surface_area(self) -> float:
        """
        Calculate total surface area in square inches.
        Used for coating/finishing estimates.
        """
        pass
    
    def get_mass_properties(self, density: float) -> MassProperties:
        """
        Calculate mass properties given material density.
        
        Returns:
            MassProperties(weight, center_of_mass, moments_of_inertia)
        """
        pass
    
    def detect_holes(self) -> List[Hole]:
        """
        Identify cylindrical features that represent holes.
        
        Returns:
            List of Hole objects with:
            - diameter
            - depth (through or blind)
            - position
            - type (plain, countersink, counterbore, threaded)
        """
        pass
    
    def detect_structural_shapes(self) -> List[StructuralShape]:
        """
        Identify standard structural shapes.
        
        Returns:
            List of detected shapes:
            - Wide flange (W shapes)
            - Channels (C shapes)
            - Angles (L shapes)
            - Tube (HSS rectangular/square)
            - Pipe (HSS round)
            - Flat bar
            - Plate
        """
        pass
    
    def count_solid_bodies(self) -> int:
        """
        Count distinct solid bodies in the model.
        Multiple bodies suggest weldment or assembly.
        """
        pass
    
    def estimate_weld_length(self) -> float:
        """
        Estimate total weld length by analyzing edge intersections
        between adjacent solid bodies.
        
        Returns:
            Estimated weld length in inches
        """
        pass
    
    def get_face_analysis(self) -> FaceAnalysis:
        """
        Analyze all faces in the model.
        
        Returns:
            FaceAnalysis with counts of:
            - planar_faces
            - cylindrical_faces
            - conical_faces
            - spherical_faces
            - freeform_faces
        """
        pass
    
    def calculate_complexity_score(self) -> float:
        """
        Calculate a 0-100 complexity score based on:
        - Face count
        - Edge count
        - Hole count and variety
        - Feature density (features per cubic inch)
        - Surface type variety
        
        Returns:
            Complexity score (0-100)
        """
        pass
    
    def detect_units(self) -> str:
        """
        Detect whether file uses mm or inches.
        
        Strategy:
        1. Check STEP header for unit declaration
        2. Analyze coordinate magnitudes
        3. Return 'mm', 'inches', or 'unknown'
        """
        pass
    
    def get_product_info(self) -> List[ProductInfo]:
        """
        Extract product/part information from STEP metadata.
        
        Returns:
            List of ProductInfo with:
            - name
            - description
            - id
        """
        pass
```

#### STEP Extraction Output Schema

```python
@dataclass
class STEPExtractionResult:
    # File Info
    filename: str
    file_size_bytes: int
    detected_units: str  # 'mm' | 'inches' | 'unknown'
    parsing_confidence: float  # 0-1
    
    # Bounding Box
    bounding_box: BoundingBox
    
    # Mass Properties
    volume_cubic_inches: float
    surface_area_sq_inches: float
    estimated_weight_lbs: Optional[float]  # If density provided
    center_of_mass: Tuple[float, float, float]
    
    # Topology
    solid_body_count: int
    face_count: int
    edge_count: int
    vertex_count: int
    
    # Face Analysis
    planar_face_count: int
    cylindrical_face_count: int
    other_face_count: int
    
    # Features
    holes: List[Hole]
    structural_shapes: List[StructuralShape]
    estimated_weld_length_inches: float
    
    # Complexity
    complexity_score: float  # 0-100
    
    # Metadata
    product_names: List[str]
    
    # Warnings
    warnings: List[str]
```

---

### 5.2 DXF File Parser

#### Supported Formats
- DXF R12 through R2018
- ASCII and Binary DXF

#### Required Libraries
```python
# Primary: ezdxf
import ezdxf
from ezdxf.entities import LWPolyline, Circle, Arc, Line, MText

# For geometry operations
from shapely.geometry import Polygon, LineString
from shapely.ops import unary_union
```

#### Extraction Requirements

```python
class DXFExtractor:
    """
    Extract geometry and features from DXF files.
    Optimized for sheet metal flat patterns and 2D cut profiles.
    """
    
    def extract(self, filepath: str) -> DXFExtractionResult:
        """
        Main extraction method.
        """
        pass
    
    def get_bounding_rectangle(self) -> BoundingRectangle:
        """
        Calculate minimum bounding rectangle.
        
        Returns:
            BoundingRectangle(width, height, area, units)
        """
        pass
    
    def get_cut_length(self) -> float:
        """
        Calculate total perimeter/cut length.
        Sum of all closed profile perimeters.
        
        Returns:
            Total cut length in inches
        """
        pass
    
    def get_pierce_count(self) -> int:
        """
        Count number of pierce points needed for laser/plasma.
        
        Returns:
            Number of closed contours (outer profile + all holes)
        """
        pass
    
    def detect_holes(self) -> List[DXFHole]:
        """
        Identify circles and arcs that represent holes.
        
        Returns:
            List of DXFHole with:
            - diameter
            - center_position
            - type (round, slotted, irregular)
        """
        pass
    
    def detect_bend_lines(self) -> List[BendLine]:
        """
        Identify bend lines based on layer naming conventions.
        
        Common layer names:
        - BEND, BENDS, BEND_LINES
        - UP, DOWN (bend direction)
        - FORM, FORMING
        
        Returns:
            List of BendLine with:
            - position
            - length
            - direction (up/down if known)
        """
        pass
    
    def get_layer_analysis(self) -> Dict[str, LayerInfo]:
        """
        Analyze all layers in the file.
        
        Returns:
            Dict mapping layer name to LayerInfo:
            - entity_count
            - entity_types
            - color
            - suggested_purpose (cut, bend, etch, text, dimension)
        """
        pass
    
    def detect_part_quantity(self) -> int:
        """
        Detect if multiple identical parts are nested.
        
        Strategy:
        1. Find repeating closed profiles
        2. Use geometric hashing for comparison
        
        Returns:
            Detected quantity (1 if unable to determine)
        """
        pass
    
    def calculate_nested_area(self) -> NestingAnalysis:
        """
        Calculate nesting efficiency metrics.
        
        Returns:
            NestingAnalysis with:
            - part_area
            - bounding_area
            - utilization_percent
            - suggested_sheet_size
        """
        pass
    
    def extract_text_and_dimensions(self) -> TextExtraction:
        """
        Extract text entities and dimensions.
        
        Returns:
            TextExtraction with:
            - part_numbers
            - dimensions
            - notes
            - tolerances
        """
        pass
    
    def validate_geometry(self) -> List[GeometryIssue]:
        """
        Check for common geometry issues.
        
        Checks:
        - Open contours (unclosed profiles)
        - Duplicate entities
        - Zero-length segments
        - Self-intersecting profiles
        
        Returns:
            List of GeometryIssue warnings
        """
        pass
```

#### DXF Extraction Output Schema

```python
@dataclass
class DXFExtractionResult:
    # File Info
    filename: str
    dxf_version: str
    detected_units: str
    parsing_confidence: float
    
    # Bounding Rectangle
    bounding_width: float
    bounding_height: float
    bounding_area: float
    
    # Cut Profile
    total_cut_length: float
    outer_perimeter: float
    pierce_count: int
    
    # Holes
    holes: List[DXFHole]
    hole_count: int
    
    # Sheet Metal
    bend_lines: List[BendLine]
    bend_count: int
    
    # Layers
    layers: Dict[str, LayerInfo]
    cut_layers: List[str]
    bend_layers: List[str]
    
    # Nesting
    part_area: float
    nesting_utilization: float
    detected_quantity: int
    
    # Text
    extracted_text: List[str]
    extracted_dimensions: List[str]
    
    # Validation
    geometry_issues: List[GeometryIssue]
    is_valid: bool
    
    # Complexity
    complexity_score: float
```

---

### 5.3 PDF Parser

#### Purpose
Extract dimensional and specification data from drawing PDFs when CAD files are unavailable or to supplement CAD data.

#### Required Libraries
```python
# PDF text extraction
import pdfplumber
from pypdf import PdfReader

# OCR for scanned drawings
import pytesseract
from pdf2image import convert_from_path

# Vision AI for complex extraction (optional)
# Claude Vision API or similar
```

#### Extraction Requirements

```python
class PDFExtractor:
    """
    Extract manufacturing data from PDF drawings.
    """
    
    def extract(self, filepath: str) -> PDFExtractionResult:
        """
        Main extraction method.
        """
        pass
    
    def extract_title_block(self) -> TitleBlock:
        """
        Extract title block information.
        
        Returns:
            TitleBlock with:
            - part_number
            - revision
            - title
            - material
            - finish
            - drawn_by
            - date
            - scale
        """
        pass
    
    def extract_bill_of_materials(self) -> List[BOMItem]:
        """
        Extract BOM if present on drawing.
        
        Returns:
            List of BOMItem with:
            - item_number
            - part_number
            - description
            - quantity
            - material
        """
        pass
    
    def extract_notes(self) -> List[str]:
        """
        Extract general notes from drawing.
        
        Returns:
            List of note strings
        """
        pass
    
    def extract_dimensions(self) -> List[Dimension]:
        """
        Extract key dimensions using OCR and pattern matching.
        
        Returns:
            List of Dimension with:
            - value
            - tolerance (if present)
            - type (linear, diameter, angle)
        """
        pass
    
    def extract_weld_symbols(self) -> List[WeldSymbol]:
        """
        Identify weld symbols and their specifications.
        
        Returns:
            List of WeldSymbol with:
            - weld_type
            - size
            - length
            - specification
        """
        pass
```

---

## 6. Feature Extraction Engine

### 6.1 Structural Shape Detection

```python
class StructuralShapeDetector:
    """
    Detect and classify standard structural steel shapes from STEP geometry.
    """
    
    SHAPE_LIBRARY = {
        'W': WideFlange,      # W8x28, W10x49, etc.
        'C': Channel,         # C6x8.2, C8x11.5, etc.
        'L': Angle,           # L4x4x1/4, L6x6x3/8, etc.
        'HSS_RECT': HSSRect,  # HSS6x4x1/4, etc.
        'HSS_SQ': HSSSquare,  # HSS4x4x1/4, etc.
        'HSS_RND': HSSRound,  # HSS4.000x0.250, etc.
        'PIPE': Pipe,         # Pipe schedules
        'FLAT': FlatBar,      # 1/2 x 4 flat, etc.
        'PLATE': Plate,       # Plate stock
        'ROUND': RoundBar,    # Round bar stock
    }
    
    def detect(self, solid_body) -> Optional[StructuralShape]:
        """
        Analyze a solid body and match to standard shape.
        
        Strategy:
        1. Extract cross-section profile
        2. Match against shape library
        3. Return best match with confidence
        """
        pass
    
    def get_cross_section(self, solid_body) -> CrossSection:
        """
        Extract cross-sectional profile of elongated shape.
        """
        pass
    
    def match_wide_flange(self, cross_section) -> Optional[WideFlange]:
        """
        Match cross-section to W-shape dimensions.
        
        Checks:
        - I-beam profile geometry
        - Flange width/thickness
        - Web depth/thickness
        - Match to AISC table
        """
        pass
    
    def match_angle(self, cross_section) -> Optional[Angle]:
        """
        Match cross-section to L-shape dimensions.
        """
        pass
    
    def match_tube(self, cross_section) -> Optional[HSS]:
        """
        Match cross-section to HSS tube dimensions.
        """
        pass
```

### 6.2 Hole Detection and Classification

```python
class HoleDetector:
    """
    Detect and classify holes from cylindrical surfaces.
    """
    
    def detect_holes(self, shape) -> List[Hole]:
        """
        Find all holes in the model.
        """
        pass
    
    def classify_hole(self, cylindrical_face) -> Hole:
        """
        Classify a cylindrical feature.
        
        Types:
        - THROUGH: Cylinder passes completely through
        - BLIND: Cylinder terminates in solid
        - COUNTERSINK: Conical entry
        - COUNTERBORE: Stepped diameter
        - THREADED: Helix detected on surface
        """
        pass
    
    def match_standard_size(self, diameter: float) -> Optional[str]:
        """
        Match hole diameter to standard drill/tap size.
        
        Returns:
            Standard size string (e.g., "1/2", "#10", "M8")
        """
        pass
    
    def detect_hole_pattern(self, holes: List[Hole]) -> Optional[HolePattern]:
        """
        Detect if holes form a pattern.
        
        Patterns:
        - BOLT_CIRCLE: Circular pattern
        - LINEAR: Row of equally spaced holes
        - GRID: Rectangular array
        """
        pass
```

### 6.3 Complexity Scoring

```python
class ComplexityScorer:
    """
    Calculate manufacturing complexity score.
    """
    
    def calculate_score(self, extraction_result) -> ComplexityScore:
        """
        Calculate overall complexity score (0-100).
        
        Factors:
        - geometry_complexity (face count, edge count)
        - feature_complexity (holes, pockets, threads)
        - tolerance_complexity (from drawing if available)
        - material_complexity (hardness, machinability)
        - size_complexity (large parts harder to handle)
        
        Returns:
            ComplexityScore with overall and component scores
        """
        pass
    
    SCORING_WEIGHTS = {
        'geometry': 0.25,
        'features': 0.30,
        'tolerances': 0.20,
        'material': 0.15,
        'size': 0.10,
    }
```

---

## 7. Process Routing Engine

### 7.1 Routing Rule Engine

```python
class RoutingEngine:
    """
    Determine manufacturing operations based on part characteristics.
    """
    
    def generate_routing(self, 
                         extraction_result: ExtractionResult,
                         material: Material,
                         quantity: int) -> ProcessRouting:
        """
        Generate complete process routing.
        
        Returns:
            ProcessRouting with ordered list of operations
        """
        pass
    
    def evaluate_rules(self, context: RoutingContext) -> List[Operation]:
        """
        Evaluate routing rules against part context.
        """
        pass
```

### 7.2 Routing Rules Configuration

```yaml
# routing_rules.yaml

rules:
  # Structural Steel Cutting
  - id: SAW_STRUCTURAL
    name: "Saw Cutting - Structural Shapes"
    conditions:
      - structural_shapes_detected: true
      - shape_type_in: [W, C, L, HSS_RECT, HSS_SQ, HSS_RND, PIPE]
    operation:
      department: SAW
      description: "Saw cut structural members to length"
      equipment: "Horizontal Band Saw"
      base_rate: 85.00
    time_calculation:
      formula: "(cut_count * 0.15) + setup_time"
      setup_time: 0.25
      variables:
        cut_count: "len(structural_shapes)"
    
  # Laser Cutting - Sheet Metal
  - id: LASER_SHEET
    name: "Laser Cutting - Sheet Metal"
    conditions:
      - file_type: DXF
      - material_thickness_lte: 0.5
    operation:
      department: LASER
      description: "Fiber laser cutting"
      equipment: "Fiber Laser"
      base_rate: 175.00
    time_calculation:
      formula: "(cut_length / cut_speed) + (pierce_count * pierce_time) + setup"
      variables:
        cut_length: "extraction.total_cut_length"
        cut_speed: 200  # inches per minute (varies by thickness)
        pierce_count: "extraction.pierce_count"
        pierce_time: 0.02  # minutes per pierce
        setup: 0.25
    thickness_adjustments:
      - max_thickness: 0.125
        cut_speed: 300
      - max_thickness: 0.25
        cut_speed: 200
      - max_thickness: 0.5
        cut_speed: 120
  
  # Plasma Cutting - Thick Plate
  - id: PLASMA_PLATE
    name: "Plasma Cutting - Plate"
    conditions:
      - file_type_in: [STEP, DXF]
      - material_thickness_gt: 0.5
      - material_thickness_lte: 2.0
    operation:
      department: BURN
      description: "Plasma cutting"
      equipment: "Plasma Table"
      base_rate: 95.00
    time_calculation:
      formula: "(cut_length / cut_speed) + (pierce_count * 0.05) + setup"
      
  # Drilling
  - id: DRILL_HOLES
    name: "Drilling Operations"
    conditions:
      - hole_count_gt: 0
    operation:
      department: DRILL
      description: "Drill holes per drawing"
      equipment: "Mag Drill / Drill Press"
      base_rate: 90.00
    time_calculation:
      formula: "(hole_count * time_per_hole) + setup"
      variables:
        hole_count: "len(extraction.holes)"
        time_per_hole: 0.08  # hours per hole (adjust by diameter/depth)
        setup: 0.25
    hole_size_adjustments:
      - max_diameter: 0.5
        time_per_hole: 0.05
      - max_diameter: 1.0
        time_per_hole: 0.08
      - max_diameter: 2.0
        time_per_hole: 0.15
        
  # Press Brake Bending
  - id: BEND_SHEET
    name: "Press Brake Bending"
    conditions:
      - bend_count_gt: 0
    operation:
      department: BRAKE
      description: "Form bends per drawing"
      equipment: "Press Brake"
      base_rate: 95.00
    time_calculation:
      formula: "(bend_count * time_per_bend) + setup"
      variables:
        bend_count: "extraction.bend_count"
        time_per_bend: 0.05
        setup: 0.25
        
  # Welding - Structural
  - id: WELD_STRUCTURAL
    name: "Welding - Structural Assembly"
    conditions:
      - solid_body_count_gt: 1
      - material_type_in: [A36, A992, A500]
    operation:
      department: WELD
      description: "Weld assembly per AWS D1.1"
      equipment: "MIG Welder (GMAW)"
      base_rate: 125.00
    time_calculation:
      formula: "(weld_length * time_per_inch) + fitup_time + setup"
      variables:
        weld_length: "extraction.estimated_weld_length"
        time_per_inch: 0.02  # fillet weld
        fitup_time: "weld_length * 0.01"
        setup: 0.5
    weld_type_adjustments:
      fillet:
        time_per_inch: 0.02
      full_penetration:
        time_per_inch: 0.05
      
  # Grinding/Deburring
  - id: GRIND_DEBURR
    name: "Grinding & Deburring"
    conditions:
      - any_cutting_operation: true
    operation:
      department: FINISH
      description: "Remove burrs, blend welds"
      equipment: "Angle Grinder"
      base_rate: 75.00
    time_calculation:
      formula: "complexity_score * 0.03 + base_time"
      variables:
        base_time: 0.25
        
  # Blast Cleaning
  - id: BLAST_CLEAN
    name: "Abrasive Blast Cleaning"
    conditions:
      - surface_prep_required: true
    operation:
      department: BLAST
      description: "Blast to SSPC-SP6 or SP10"
      equipment: "Blast Cabinet/Room"
      base_rate: 90.00
    time_calculation:
      formula: "surface_area_sqft * time_per_sqft + setup"
      variables:
        surface_area_sqft: "extraction.surface_area / 144"
        time_per_sqft: 0.02
        setup: 0.25
        
  # Primer Coating
  - id: PRIME_COAT
    name: "Prime Coating"
    conditions:
      - primer_required: true
    operation:
      department: PAINT
      description: "Apply primer coat"
      equipment: "Spray Booth"
      base_rate: 90.00
    time_calculation:
      formula: "surface_area_sqft * time_per_sqft + setup"
      variables:
        time_per_sqft: 0.01
        setup: 0.25
        
  # QC Inspection
  - id: QC_INSPECT
    name: "Quality Inspection"
    conditions:
      - always: true
    operation:
      department: QC
      description: "Dimensional and visual inspection"
      equipment: "Inspection Tools"
      base_rate: 90.00
    time_calculation:
      formula: "base_time + (complexity_score * 0.01)"
      variables:
        base_time: 0.25
```

### 7.3 Time Estimation

```python
class TimeEstimator:
    """
    Calculate operation time based on geometry and rules.
    """
    
    def estimate_saw_time(self, 
                          cuts: int, 
                          material: Material,
                          shape_type: str) -> float:
        """
        Estimate saw cutting time.
        
        Factors:
        - Number of cuts
        - Material hardness
        - Cross-section size
        - Shape complexity (coping required?)
        """
        pass
    
    def estimate_laser_time(self,
                            cut_length: float,
                            pierce_count: int,
                            thickness: float,
                            material: Material) -> float:
        """
        Estimate laser cutting time.
        
        Uses IPM (inches per minute) lookup tables
        based on material and thickness.
        """
        pass
    
    def estimate_weld_time(self,
                           weld_length: float,
                           weld_type: str,
                           position: str,
                           material: Material) -> float:
        """
        Estimate welding time.
        
        Factors:
        - Weld length
        - Weld type (fillet, groove, full pen)
        - Position (flat, horizontal, vertical, overhead)
        - Material (steel vs aluminum vs stainless)
        - Includes fit-up time
        """
        pass
    
    def estimate_drill_time(self,
                            holes: List[Hole],
                            material: Material) -> float:
        """
        Estimate drilling time.
        
        Factors:
        - Hole count
        - Hole diameter
        - Hole depth
        - Material hardness
        - Tool changes
        """
        pass
```

---

## 8. Cost Calculation Engine

### 8.1 Material Cost Calculator

```python
class MaterialCostCalculator:
    """
    Calculate material costs with scrap factor.
    """
    
    def calculate(self,
                  extraction: ExtractionResult,
                  material: Material,
                  quantity: int,
                  scrap_factor: float = 0.25) -> MaterialCost:
        """
        Calculate total material cost.
        
        Returns:
            MaterialCost with:
            - raw_material_items
            - base_cost
            - scrap_cost
            - total_cost
        """
        pass
    
    def estimate_stock_size(self, 
                            bounding_box: BoundingBox,
                            material_form: str) -> StockSize:
        """
        Determine optimal stock size for the part.
        
        Material forms:
        - PLATE: Select from standard plate sizes
        - BAR: Select from standard bar lengths
        - TUBE: Select from standard tube lengths
        - STRUCTURAL: Select from standard mill lengths
        """
        pass
    
    def lookup_material_price(self,
                              material: Material,
                              form: str,
                              size: str) -> float:
        """
        Look up current material pricing.
        
        Sources:
        - Internal price database
        - Supplier API (future)
        - Manual override
        """
        pass
```

### 8.2 Labor Cost Calculator

```python
class LaborCostCalculator:
    """
    Calculate labor costs from routing.
    """
    
    def calculate(self, routing: ProcessRouting) -> LaborCost:
        """
        Calculate total labor cost.
        
        Returns:
            LaborCost with:
            - operations (with hours and cost each)
            - total_hours
            - total_cost
        """
        pass
    
    def get_labor_rate(self, department: str) -> float:
        """
        Get fully-burdened labor rate for department.
        """
        pass
```

### 8.3 Consumables Calculator

```python
class ConsumablesCalculator:
    """
    Calculate consumables costs.
    """
    
    def calculate(self, 
                  routing: ProcessRouting,
                  material: Material) -> ConsumablesCost:
        """
        Calculate consumables for all operations.
        
        Includes:
        - Welding wire and gas
        - Cutting consumables (blades, tips, gas)
        - Abrasives
        - Coatings (primer, paint)
        """
        pass
    
    CONSUMABLE_RATES = {
        'weld_wire_per_lb': 3.50,
        'shield_gas_per_cf': 0.15,
        'saw_blade_per_cut': 0.50,
        'drill_bit_per_hole': 0.10,
        'grinding_disc_per_hour': 5.00,
        'primer_per_sqft': 0.25,
        'blast_media_per_sqft': 0.10,
    }
```

### 8.4 Quote Builder

```python
class QuoteBuilder:
    """
    Assemble complete quote from components.
    """
    
    def build(self,
              material_cost: MaterialCost,
              labor_cost: LaborCost,
              consumables_cost: ConsumablesCost,
              margin_percent: float,
              quantity: int) -> Quote:
        """
        Build complete quote.
        
        Returns:
            Quote with:
            - line_items
            - material_total
            - labor_total
            - consumables_total
            - subtotal
            - margin_amount
            - total_price
            - unit_price
        """
        pass
    
    def apply_quantity_breaks(self, 
                              base_price: float, 
                              quantity: int) -> float:
        """
        Apply quantity discount if applicable.
        """
        pass
```

---

## 9. Data Models

### 9.1 Core Entities

```python
# models/quote.py

from dataclasses import dataclass
from typing import List, Optional, Dict
from datetime import datetime
from enum import Enum

class QuoteStatus(Enum):
    DRAFT = "draft"
    INTERNAL_REVIEW = "internal_review"
    SENT = "sent"
    WON = "won"
    LOST = "lost"
    EXPIRED = "expired"

@dataclass
class Quote:
    id: str
    quote_number: str
    customer_id: str
    customer_name: str
    project_name: str
    status: QuoteStatus
    created_at: datetime
    updated_at: datetime
    valid_until: datetime
    created_by: str
    
    # Pricing
    material_total: float
    labor_total: float
    consumables_total: float
    subtotal: float
    margin_percent: float
    margin_amount: float
    total_price: float
    
    # Content
    line_items: List['QuoteLineItem']
    notes: List[str]
    terms: List[str]
    
    # Metadata
    source_files: List[str]
    confidence_score: float

@dataclass
class QuoteLineItem:
    id: str
    quote_id: str
    line_number: int
    part_number: str
    description: str
    quantity: int
    unit_price: float
    extended_price: float
    
    # Breakdown
    material_cost: float
    labor_cost: float
    labor_hours: float
    consumables_cost: float
    
    # References
    part_geometry_id: Optional[str]
    process_routing_id: Optional[str]

@dataclass
class PartGeometry:
    id: str
    source_file: str
    file_type: str  # STEP, DXF, PDF
    extraction_timestamp: datetime
    
    # Bounding Box
    bbox_length: float
    bbox_width: float
    bbox_height: float
    
    # Properties
    volume: Optional[float]
    surface_area: Optional[float]
    weight_estimate: Optional[float]
    
    # Features
    hole_count: int
    holes: List[Dict]  # JSON
    solid_body_count: int
    structural_shapes: List[Dict]  # JSON
    bend_count: int
    
    # Metrics
    complexity_score: float
    cut_length: Optional[float]
    weld_length_estimate: Optional[float]
    
    # Raw extraction
    raw_extraction: Dict  # Full extraction result as JSON

@dataclass
class ProcessRouting:
    id: str
    part_geometry_id: str
    created_at: datetime
    
    # Operations
    operations: List['Operation']
    total_hours: float
    
    # Routing metadata
    routing_rules_version: str
    manual_overrides: List[Dict]

@dataclass
class Operation:
    op_number: int  # 10, 20, 30...
    department: str
    description: str
    equipment: str
    setup_hours: float
    run_hours: float
    total_hours: float
    labor_rate: float
    extended_cost: float
    notes: Optional[str]
    
    # Calculation trace
    time_formula: str
    time_variables: Dict

@dataclass
class Material:
    id: str
    name: str
    specification: str  # A36, 6061-T6, 304SS, etc.
    form: str  # plate, bar, tube, sheet, structural
    
    # Properties
    density: float  # lb/in³
    machinability_rating: float  # 0-1
    weldability_rating: float  # 0-1
    
    # Pricing
    unit_cost: float
    unit_of_measure: str  # lb, ft, sqft
    last_price_update: datetime
    
    # Defaults
    default_scrap_factor: float

@dataclass
class LaborRate:
    id: str
    department: str
    operation_type: str
    hourly_rate: float
    is_burdened: bool
    effective_date: datetime
    
@dataclass
class Customer:
    id: str
    name: str
    address: str
    city: str
    state: str
    zip: str
    contact_name: str
    contact_email: str
    contact_phone: str
    payment_terms: str
    default_margin: float
```

### 9.2 Database Schema

```sql
-- PostgreSQL Schema

-- Quotes
CREATE TABLE quotes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    quote_number VARCHAR(50) UNIQUE NOT NULL,
    customer_id UUID REFERENCES customers(id),
    project_name VARCHAR(255),
    status VARCHAR(50) NOT NULL DEFAULT 'draft',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    valid_until DATE,
    created_by VARCHAR(100),
    
    material_total DECIMAL(12,2),
    labor_total DECIMAL(12,2),
    consumables_total DECIMAL(12,2),
    subtotal DECIMAL(12,2),
    margin_percent DECIMAL(5,2),
    margin_amount DECIMAL(12,2),
    total_price DECIMAL(12,2),
    
    notes JSONB,
    terms JSONB,
    source_files JSONB,
    confidence_score DECIMAL(5,2)
);

-- Quote Line Items
CREATE TABLE quote_line_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    quote_id UUID REFERENCES quotes(id) ON DELETE CASCADE,
    line_number INTEGER NOT NULL,
    part_number VARCHAR(100),
    description TEXT,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(12,2),
    extended_price DECIMAL(12,2),
    
    material_cost DECIMAL(12,2),
    labor_cost DECIMAL(12,2),
    labor_hours DECIMAL(8,2),
    consumables_cost DECIMAL(12,2),
    
    part_geometry_id UUID REFERENCES part_geometries(id),
    process_routing_id UUID REFERENCES process_routings(id),
    
    UNIQUE(quote_id, line_number)
);

-- Part Geometries
CREATE TABLE part_geometries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_file VARCHAR(500),
    file_type VARCHAR(20),
    extraction_timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    bbox_length DECIMAL(12,4),
    bbox_width DECIMAL(12,4),
    bbox_height DECIMAL(12,4),
    
    volume DECIMAL(16,6),
    surface_area DECIMAL(16,4),
    weight_estimate DECIMAL(12,4),
    
    hole_count INTEGER,
    holes JSONB,
    solid_body_count INTEGER,
    structural_shapes JSONB,
    bend_count INTEGER,
    
    complexity_score DECIMAL(5,2),
    cut_length DECIMAL(12,4),
    weld_length_estimate DECIMAL(12,4),
    
    raw_extraction JSONB
);

-- Process Routings
CREATE TABLE process_routings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    part_geometry_id UUID REFERENCES part_geometries(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    operations JSONB NOT NULL,
    total_hours DECIMAL(8,2),
    
    routing_rules_version VARCHAR(50),
    manual_overrides JSONB
);

-- Materials
CREATE TABLE materials (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    specification VARCHAR(100),
    form VARCHAR(50),
    
    density DECIMAL(8,6),
    machinability_rating DECIMAL(3,2),
    weldability_rating DECIMAL(3,2),
    
    unit_cost DECIMAL(10,4),
    unit_of_measure VARCHAR(20),
    last_price_update TIMESTAMP WITH TIME ZONE,
    
    default_scrap_factor DECIMAL(4,2) DEFAULT 0.25
);

-- Labor Rates
CREATE TABLE labor_rates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    department VARCHAR(50) NOT NULL,
    operation_type VARCHAR(100),
    hourly_rate DECIMAL(8,2) NOT NULL,
    is_burdened BOOLEAN DEFAULT TRUE,
    effective_date DATE NOT NULL,
    
    UNIQUE(department, operation_type, effective_date)
);

-- Customers
CREATE TABLE customers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    zip VARCHAR(20),
    contact_name VARCHAR(100),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(50),
    payment_terms VARCHAR(100),
    default_margin DECIMAL(5,2) DEFAULT 40.00
);

-- Indexes
CREATE INDEX idx_quotes_customer ON quotes(customer_id);
CREATE INDEX idx_quotes_status ON quotes(status);
CREATE INDEX idx_quotes_created ON quotes(created_at);
CREATE INDEX idx_line_items_quote ON quote_line_items(quote_id);
CREATE INDEX idx_geometries_file ON part_geometries(source_file);
```

---

## 10. API Specifications

### 10.1 REST API Endpoints

```yaml
openapi: 3.0.0
info:
  title: QuoteEngine API
  version: 1.0.0

paths:
  # File Upload & Processing
  /api/files/upload:
    post:
      summary: Upload CAD file for processing
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
                file_type:
                  type: string
                  enum: [STEP, DXF, PDF]
      responses:
        200:
          description: File uploaded and queued for processing
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileUploadResponse'

  /api/files/{file_id}/extraction:
    get:
      summary: Get extraction results for uploaded file
      parameters:
        - name: file_id
          in: path
          required: true
          schema:
            type: string
      responses:
        200:
          description: Extraction results
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExtractionResult'

  # Quotes
  /api/quotes:
    get:
      summary: List quotes
      parameters:
        - name: status
          in: query
          schema:
            type: string
        - name: customer_id
          in: query
          schema:
            type: string
        - name: limit
          in: query
          schema:
            type: integer
            default: 50
        - name: offset
          in: query
          schema:
            type: integer
            default: 0
      responses:
        200:
          description: List of quotes
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/QuoteSummary'
    
    post:
      summary: Create new quote
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateQuoteRequest'
      responses:
        201:
          description: Quote created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Quote'

  /api/quotes/{quote_id}:
    get:
      summary: Get quote details
      responses:
        200:
          description: Quote details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Quote'
    
    put:
      summary: Update quote
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateQuoteRequest'
      responses:
        200:
          description: Quote updated

  /api/quotes/{quote_id}/generate-routing:
    post:
      summary: Generate process routing for quote line items
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                line_item_ids:
                  type: array
                  items:
                    type: string
                material_id:
                  type: string
                options:
                  type: object
      responses:
        200:
          description: Routing generated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProcessRouting'

  /api/quotes/{quote_id}/calculate:
    post:
      summary: Calculate quote pricing
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                margin_percent:
                  type: number
                scrap_factor:
                  type: number
      responses:
        200:
          description: Quote calculated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Quote'

  /api/quotes/{quote_id}/documents:
    post:
      summary: Generate quote document
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                format:
                  type: string
                  enum: [pdf, docx, xlsx]
                template:
                  type: string
                  enum: [internal_review, customer_quote, process_traveler]
      responses:
        200:
          description: Document generated
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary

  # Materials
  /api/materials:
    get:
      summary: List materials
      responses:
        200:
          description: List of materials
    
    post:
      summary: Create material
      responses:
        201:
          description: Material created

  /api/materials/{material_id}:
    get:
      summary: Get material details
    put:
      summary: Update material
    delete:
      summary: Delete material

  # Labor Rates
  /api/labor-rates:
    get:
      summary: List labor rates
    post:
      summary: Create labor rate

  # Customers
  /api/customers:
    get:
      summary: List customers
    post:
      summary: Create customer

  # Similar Parts
  /api/similar-parts:
    post:
      summary: Find similar parts from history
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                geometry_id:
                  type: string
                limit:
                  type: integer
                  default: 5
      responses:
        200:
          description: Similar parts found
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SimilarPart'

components:
  schemas:
    FileUploadResponse:
      type: object
      properties:
        file_id:
          type: string
        filename:
          type: string
        status:
          type: string
          enum: [queued, processing, completed, failed]
        
    ExtractionResult:
      type: object
      properties:
        file_id:
          type: string
        file_type:
          type: string
        extraction_timestamp:
          type: string
          format: date-time
        confidence_score:
          type: number
        bounding_box:
          $ref: '#/components/schemas/BoundingBox'
        volume:
          type: number
        surface_area:
          type: number
        holes:
          type: array
          items:
            $ref: '#/components/schemas/Hole'
        complexity_score:
          type: number
        warnings:
          type: array
          items:
            type: string
            
    BoundingBox:
      type: object
      properties:
        length:
          type: number
        width:
          type: number
        height:
          type: number
        units:
          type: string
          
    Hole:
      type: object
      properties:
        diameter:
          type: number
        depth:
          type: number
        type:
          type: string
          enum: [through, blind, countersink, counterbore, threaded]
        position:
          type: array
          items:
            type: number
            
    Quote:
      type: object
      properties:
        id:
          type: string
        quote_number:
          type: string
        customer_name:
          type: string
        project_name:
          type: string
        status:
          type: string
        total_price:
          type: number
        line_items:
          type: array
          items:
            $ref: '#/components/schemas/QuoteLineItem'
            
    QuoteLineItem:
      type: object
      properties:
        id:
          type: string
        part_number:
          type: string
        description:
          type: string
        quantity:
          type: integer
        unit_price:
          type: number
        extended_price:
          type: number
        labor_hours:
          type: number
          
    ProcessRouting:
      type: object
      properties:
        id:
          type: string
        operations:
          type: array
          items:
            $ref: '#/components/schemas/Operation'
        total_hours:
          type: number
          
    Operation:
      type: object
      properties:
        op_number:
          type: integer
        department:
          type: string
        description:
          type: string
        equipment:
          type: string
        hours:
          type: number
        rate:
          type: number
        cost:
          type: number
```

---

## 11. User Interface Requirements

### 11.1 Key Screens

#### Dashboard
- Quote pipeline overview (draft, sent, won, lost)
- Recent quotes
- Quick stats (win rate, average margin, quote volume)
- Action items (quotes expiring, pending review)

#### File Upload
- Drag-and-drop upload area
- Multi-file support
- Upload progress indicator
- File type validation
- Preview of extraction results

#### Extraction Review
- 3D viewer for STEP files (three.js)
- 2D viewer for DXF files
- Extracted data summary
- Feature highlights (holes, bends, structural shapes)
- Manual correction interface
- Confidence indicators

#### Quote Builder
- Customer selection
- Line item management
- Material selection per line
- Process routing view/edit
- Cost breakdown (material, labor, consumables)
- Margin adjustment
- Real-time total calculation

#### Routing Editor
- Operation list (drag to reorder)
- Time adjustment per operation
- Add/remove operations
- Equipment selection
- Notes per operation

#### Quote Output
- Preview before generate
- Template selection
- Format selection (PDF, DOCX, XLSX)
- Download or email

### 11.2 UI Components

```
/components
  /upload
    FileDropZone.tsx
    UploadProgress.tsx
    FileTypeIcon.tsx
  /viewers
    STEPViewer.tsx      # three.js based
    DXFViewer.tsx       # canvas based
    PDFViewer.tsx       # pdf.js based
  /extraction
    ExtractionSummary.tsx
    FeatureList.tsx
    BoundingBoxDisplay.tsx
    HoleTable.tsx
    ConfidenceIndicator.tsx
  /quote
    QuoteHeader.tsx
    LineItemTable.tsx
    MaterialSelector.tsx
    CostBreakdown.tsx
    MarginSlider.tsx
    TotalDisplay.tsx
  /routing
    OperationList.tsx
    OperationCard.tsx
    TimeEditor.tsx
    EquipmentSelector.tsx
  /common
    DataTable.tsx
    SearchBar.tsx
    StatusBadge.tsx
    ConfirmDialog.tsx
```

---

## 12. Output Generation

### 12.1 Document Templates

#### Internal Review Quote
- Full cost breakdown
- Process routing detail
- Labor hours by operation
- Assumptions and risks
- Approval signatures
- Review notes section

#### Customer Quote
- Professional header with logo
- Quote summary
- Line item pricing (no cost breakdown)
- Terms and conditions
- Validity period
- Acceptance signature

#### Process Traveler
- Operation sequence
- Work instructions
- Quality checkpoints
- Material traceability
- Operator sign-off

### 12.2 Document Generation

```python
class DocumentGenerator:
    """
    Generate quote documents in various formats.
    """
    
    def generate_internal_review(self, quote: Quote) -> bytes:
        """Generate detailed internal review document."""
        pass
    
    def generate_customer_quote(self, quote: Quote) -> bytes:
        """Generate customer-facing quote."""
        pass
    
    def generate_process_traveler(self, quote: Quote) -> bytes:
        """Generate shop floor traveler."""
        pass
    
    def generate_cut_list(self, quote: Quote) -> bytes:
        """Generate material cut list."""
        pass
    
    # Output formats
    def to_pdf(self, content) -> bytes:
        pass
    
    def to_docx(self, content) -> bytes:
        pass
    
    def to_xlsx(self, content) -> bytes:
        pass
```

---

## 13. Accuracy & Validation

### 13.1 Accuracy Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| Bounding box accuracy | ±0.1% | Compare to CAD system |
| Volume accuracy | ±1% | Compare to CAD system |
| Hole detection | 95% recall | Manual verification |
| Structural shape detection | 90% accuracy | Manual verification |
| Time estimate accuracy | ±15% | Actual vs estimated |
| Cost estimate accuracy | ±10% | Actual vs estimated |

### 13.2 Validation Approach

```python
class AccuracyValidator:
    """
    Validate extraction and estimation accuracy.
    """
    
    def validate_extraction(self, 
                            extraction: ExtractionResult,
                            ground_truth: GroundTruth) -> ValidationResult:
        """
        Compare extraction to known ground truth.
        """
        pass
    
    def validate_time_estimate(self,
                               estimated_hours: float,
                               actual_hours: float) -> float:
        """
        Calculate estimation error percentage.
        """
        return abs(estimated_hours - actual_hours) / actual_hours * 100
    
    def generate_accuracy_report(self, 
                                 quotes: List[Quote],
                                 actuals: List[Actual]) -> AccuracyReport:
        """
        Generate accuracy report across multiple quotes.
        
        Metrics:
        - Mean Absolute Percentage Error (MAPE)
        - Bias (over/under estimation tendency)
        - Accuracy by operation type
        - Accuracy by part complexity
        """
        pass
```

### 13.3 Confidence Scoring

```python
class ConfidenceScorer:
    """
    Calculate confidence score for extractions and quotes.
    """
    
    def score_extraction(self, result: ExtractionResult) -> float:
        """
        Score extraction confidence (0-100).
        
        Factors:
        - File parsed without errors
        - Units detected confidently
        - No geometry warnings
        - Features recognized cleanly
        """
        pass
    
    def score_routing(self, routing: ProcessRouting) -> float:
        """
        Score routing confidence.
        
        Factors:
        - All operations matched by rules
        - No manual overrides needed
        - Similar parts found in history
        """
        pass
    
    CONFIDENCE_THRESHOLDS = {
        'high': 90,      # Auto-approve
        'medium': 70,    # Review recommended
        'low': 50,       # Manual intervention needed
        'reject': 0,     # Cannot process reliably
    }
```

---

## 14. Development Phases

### Phase 1: Core Engine (MVP) - 12 Weeks

#### Weeks 1-4: File Parsing
- [ ] STEP parser with PythonOCC
- [ ] DXF parser with ezdxf
- [ ] Basic geometry extraction (bbox, volume, area)
- [ ] Hole detection
- [ ] Unit detection

#### Weeks 5-8: Routing & Costing
- [ ] Rule engine framework
- [ ] Basic routing rules (saw, drill, weld, blast, paint)
- [ ] Time calculation formulas
- [ ] Material cost calculator
- [ ] Labor cost calculator
- [ ] Consumables calculator

#### Weeks 9-12: Output & UI
- [ ] Quote data model and database
- [ ] Basic REST API
- [ ] Simple web UI for upload and review
- [ ] PDF quote generation
- [ ] Internal review document generation

### Phase 2: Intelligence - 10 Weeks

#### Weeks 13-16: Advanced Extraction
- [ ] Structural shape detection
- [ ] Weld length estimation
- [ ] Bend line detection (DXF)
- [ ] Complexity scoring
- [ ] PDF drawing parsing

#### Weeks 17-20: Smart Routing
- [ ] Expanded rule library
- [ ] Thickness-based routing adjustments
- [ ] Material-specific routing
- [ ] Similar part matching (vector similarity)
- [ ] Learning from actuals

#### Weeks 21-22: Enhanced UI
- [ ] 3D STEP viewer
- [ ] 2D DXF viewer
- [ ] Routing editor
- [ ] Manual override workflow

### Phase 3: Integration - 8 Weeks

#### Weeks 23-26: External Integrations
- [ ] ERP integration (API framework)
- [ ] Material pricing API
- [ ] Customer portal (quote requests)

#### Weeks 27-30: Analytics & Optimization
- [ ] Quote win/loss tracking
- [ ] Accuracy analytics dashboard
- [ ] Margin optimization suggestions
- [ ] Lead time forecasting

---

## 15. Technology Stack

### Backend
- **Language:** Python 3.11+
- **Framework:** FastAPI
- **Database:** PostgreSQL 15+
- **Cache:** Redis
- **Task Queue:** Celery with Redis broker
- **File Storage:** S3-compatible (MinIO for self-hosted)

### CAD Processing
- **STEP Parsing:** PythonOCC (OpenCASCADE bindings)
- **DXF Parsing:** ezdxf
- **PDF Parsing:** pdfplumber, pypdf, pytesseract
- **Geometry Operations:** Shapely, NumPy

### Frontend
- **Framework:** React 18+ with TypeScript
- **UI Components:** shadcn/ui
- **State Management:** Zustand or React Query
- **3D Viewer:** three.js
- **2D Viewer:** Canvas API or Fabric.js

### Document Generation
- **DOCX:** python-docx
- **PDF:** ReportLab or WeasyPrint
- **XLSX:** openpyxl

### DevOps
- **Containerization:** Docker
- **Orchestration:** Docker Compose (dev), Kubernetes (prod)
- **CI/CD:** GitHub Actions
- **Monitoring:** Prometheus + Grafana

---

## 16. Testing Requirements

### 16.1 Unit Tests

```python
# tests/test_step_extractor.py

def test_bounding_box_extraction():
    """Test bounding box calculation accuracy."""
    extractor = STEPExtractor()
    result = extractor.extract("fixtures/simple_block.step")
    
    assert abs(result.bounding_box.length - 10.0) < 0.01
    assert abs(result.bounding_box.width - 5.0) < 0.01
    assert abs(result.bounding_box.height - 2.0) < 0.01

def test_hole_detection():
    """Test hole detection and classification."""
    extractor = STEPExtractor()
    result = extractor.extract("fixtures/plate_with_holes.step")
    
    assert len(result.holes) == 8
    assert sum(1 for h in result.holes if h.type == 'through') == 6
    assert sum(1 for h in result.holes if h.type == 'counterbore') == 2

def test_unit_detection_mm():
    """Test millimeter unit detection."""
    extractor = STEPExtractor()
    result = extractor.extract("fixtures/part_mm.step")
    
    assert result.detected_units == 'mm'

def test_unit_detection_inches():
    """Test inch unit detection."""
    extractor = STEPExtractor()
    result = extractor.extract("fixtures/part_inches.step")
    
    assert result.detected_units == 'inches'
```

### 16.2 Integration Tests

```python
# tests/test_quote_workflow.py

def test_full_quote_workflow():
    """Test complete quote generation workflow."""
    # Upload file
    file_response = client.post("/api/files/upload", files={"file": step_file})
    file_id = file_response.json()["file_id"]
    
    # Wait for extraction
    extraction = wait_for_extraction(file_id)
    assert extraction["confidence_score"] > 0.8
    
    # Create quote
    quote_response = client.post("/api/quotes", json={
        "customer_id": customer_id,
        "project_name": "Test Project",
        "line_items": [{
            "part_geometry_id": extraction["geometry_id"],
            "quantity": 4,
            "material_id": material_id
        }]
    })
    quote_id = quote_response.json()["id"]
    
    # Generate routing
    routing_response = client.post(f"/api/quotes/{quote_id}/generate-routing")
    assert routing_response.status_code == 200
    
    # Calculate pricing
    calc_response = client.post(f"/api/quotes/{quote_id}/calculate", json={
        "margin_percent": 40,
        "scrap_factor": 0.25
    })
    
    quote = calc_response.json()
    assert quote["total_price"] > 0
    assert len(quote["line_items"]) == 1
```

### 16.3 Accuracy Test Suite

```python
# tests/test_accuracy.py

ACCURACY_TEST_CASES = [
    {
        "file": "fixtures/accuracy/simple_plate.step",
        "expected_bbox": (12.0, 8.0, 0.5),
        "expected_volume": 48.0,
        "expected_holes": 4,
    },
    {
        "file": "fixtures/accuracy/weldment_frame.step",
        "expected_bodies": 6,
        "expected_weld_length_range": (80, 120),
    },
    # Add more test cases...
]

@pytest.mark.parametrize("test_case", ACCURACY_TEST_CASES)
def test_extraction_accuracy(test_case):
    """Validate extraction accuracy against known parts."""
    extractor = STEPExtractor()
    result = extractor.extract(test_case["file"])
    
    if "expected_bbox" in test_case:
        bbox = test_case["expected_bbox"]
        assert abs(result.bounding_box.length - bbox[0]) / bbox[0] < 0.001
        assert abs(result.bounding_box.width - bbox[1]) / bbox[1] < 0.001
        assert abs(result.bounding_box.height - bbox[2]) / bbox[2] < 0.001
```

---

## Appendix A: Sample Routing Rules

See `routing_rules.yaml` in Section 7.2.

## Appendix B: Material Database Seed

```sql
INSERT INTO materials (name, specification, form, density, unit_cost, unit_of_measure) VALUES
('A36 Plate', 'ASTM A36', 'plate', 0.284, 0.85, 'lb'),
('A36 Flat Bar', 'ASTM A36', 'bar', 0.284, 0.95, 'lb'),
('A992 Wide Flange', 'ASTM A992', 'structural', 0.284, 0.85, 'lb'),
('A500 HSS Rect', 'ASTM A500 Gr B', 'tube', 0.284, 1.10, 'lb'),
('A500 HSS Round', 'ASTM A500 Gr B', 'tube', 0.284, 1.15, 'lb'),
('6061-T6 Plate', '6061-T6', 'plate', 0.098, 3.50, 'lb'),
('6061-T6 Bar', '6061-T6', 'bar', 0.098, 3.75, 'lb'),
('304 SS Plate', '304 Stainless', 'plate', 0.289, 4.50, 'lb'),
('304 SS Sheet', '304 Stainless', 'sheet', 0.289, 4.75, 'lb');
```

## Appendix C: Labor Rate Seed

```sql
INSERT INTO labor_rates (department, operation_type, hourly_rate, is_burdened) VALUES
('ENG', 'Engineering', 115.00, true),
('SAW', 'Saw Cutting', 85.00, true),
('LASER', 'Laser Cutting', 175.00, true),
('PLASMA', 'Plasma Cutting', 95.00, true),
('DRILL', 'Drilling', 90.00, true),
('BRAKE', 'Press Brake', 95.00, true),
('WELD', 'Welding - MIG', 125.00, true),
('WELD', 'Welding - TIG', 135.00, true),
('GRIND', 'Grinding', 75.00, true),
('BLAST', 'Blast Cleaning', 90.00, true),
('PAINT', 'Painting', 90.00, true),
('QC', 'Inspection', 90.00, true),
('ASSY', 'Assembly', 80.00, true);
```

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Jan 2026 | Werco Manufacturing | Initial specification |

---

*End of Document*

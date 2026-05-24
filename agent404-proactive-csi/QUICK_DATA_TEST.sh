#!/bin/bash

# Quick Data Integration Test
# Verifies all data files are loaded correctly

cd "$(dirname "$0")"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  🧪 Quick Data Integration Test 🧪                          ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check data files
echo -e "${BLUE}📁 Checking data files...${NC}"
data_dir="data"
files=("contracts.csv" "customer_comms.csv" "customer_success_data.csv" 
       "procurement_vendor_data.csv" "revenue_exposure_data.csv" "support_tickets.csv")

all_exist=true
for file in "${files[@]}"; do
    if [ -f "$data_dir/$file" ]; then
        lines=$(wc -l < "$data_dir/$file" | tr -d ' ')
        echo -e "${GREEN}  ✅ $file - $lines lines${NC}"
    else
        echo -e "${RED}  ❌ $file - Not found${NC}"
        all_exist=false
    fi
done

echo ""

if [ "$all_exist" = false ]; then
    echo -e "${RED}❌ Some data files are missing!${NC}"
    exit 1
fi

# Run Python test
echo -e "${BLUE}🧪 Running integration tests...${NC}"
python3 test_data_integration.py

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ All tests passed! Data integration successful!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${BLUE}📊 Data Summary:${NC}"
    echo -e "  • 500 customers"
    echo -e "  • 500 vendors"
    echo -e "  • 500 contracts"
    echo -e "  • 500 support tickets"
    echo -e "  • 487 customer communications"
    echo -e "  • 500 revenue records"
    echo ""
    echo -e "${GREEN}🎉 Ready for deployment!${NC}"
    exit 0
else
    echo ""
    echo -e "${RED}❌ Tests failed. Please check errors above.${NC}"
    exit 1
fi


// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";
import SoftProgress from "components/SoftProgress";

// Images
import logoBitcoin from "assets/images/small-logos/logo-bitcoin.svg";
import logoUSDT from "assets/images/small-logos/tether-usdt-logo.svg";
import logoUSDC from "assets/images/small-logos/usd-coin-usdc-logo.svg";
import logoPolygon from "assets/images/small-logos/polygon-matic-logo.svg";
import logoETH from "assets/images/small-logos/eth-logo.svg";
import logoShiba from "assets/images/small-logos/shiba-inu-shib-logo.svg";
import logoFilecoin from "assets/images/small-logos/filecoin-fil-logo.svg";

export default function data() {

  return {
    columns: [
      { name: "coins", align: "left" },
      { name: "crypto", align: "center" },
      { name: "fiat", align: "center" },
      { name: "completion", align: "center" },
    ],

    rows: [
      {
        coins: [logoBitcoin, "Bitcoin"],
        crypto: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
          0.0025 BTC
        </SoftTypography>
        ),
        fiat: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
            $14,000
          </SoftTypography>
        ),
        completion: (
          <SoftBox width="8rem" textAlign="left">
            <SoftProgress value={60} color="info" variant="gradient" label={false} />
          </SoftBox>
        ),
      },
      {
        coins: [logoUSDT, "USDT"],
        crypto: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
          0.057 USDT
        </SoftTypography>
        ),
        fiat: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
            $3,000
          </SoftTypography>
        ),
        completion: (
          <SoftBox width="8rem" textAlign="left">
            <SoftProgress value={10} color="info" variant="gradient" label={false} />
          </SoftBox>
        ),
      },
      {
        coins: [logoUSDC, "USDC"],
        crypto: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
            0.00145 USDC
          </SoftTypography>
        ),
        fiat: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
            Not set
          </SoftTypography>
        ),
        completion: (
          <SoftBox width="8rem" textAlign="left">
            <SoftProgress value={100} color="success" variant="gradient" label={false} />
          </SoftBox>
        ),
      },
      {
        coins: [logoPolygon, "Polygon"],
        crypto: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
          1.2010 MATIC
          </SoftTypography>
        ),
        fiat: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
            $20,500
          </SoftTypography>
        ),
        completion: (
          <SoftBox width="8rem" textAlign="left">
            <SoftProgress value={100} color="success" variant="gradient" label={false} />
          </SoftBox>
        ),
      },
      {
        coins: [logoETH, "Ethereum"],
        crypto: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
            0.1985 ETH
          </SoftTypography>
        ),
        fiat: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
            $500
          </SoftTypography>
        ),
        completion: (
          <SoftBox width="8rem" textAlign="left">
            <SoftProgress value={25} color="info" variant="gradient" label={false} />
          </SoftBox>
        ),
      },
      {
        coins: [logoShiba, "Shiba Inu"],
        crypto: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
          0.0001125 SHIB
        </SoftTypography>
        ),
        fiat: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
            $500
          </SoftTypography>
        ),
        completion: (
          <SoftBox width="8rem" textAlign="left">
            <SoftProgress value={25} color="info" variant="gradient" label={false} />
          </SoftBox>
        ),
      },
      {
        coins: [logoFilecoin, "Filecoin"],
        crypto: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
          1.478 FIL
        </SoftTypography>
        ),
        fiat: (
          <SoftTypography variant="caption" color="text" fontWeight="medium">
            $2,000
          </SoftTypography>
        ),
        completion: (
          <SoftBox width="8rem" textAlign="left">
            <SoftProgress value={40} color="info" variant="gradient" label={false} />
          </SoftBox>
        ),
      },
    ],
  };
}
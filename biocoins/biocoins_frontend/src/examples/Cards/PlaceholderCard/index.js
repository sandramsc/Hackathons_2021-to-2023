// prop-types is a library for typechecking of props
import PropTypes from "prop-types";

// clsx is a utility for constructing className strings conditionally
import clsx from "clsx";

// @mui material components
import Card from "@mui/material/Card";
import Icon from "@mui/material/Icon";

// Soft UI Dashboard React components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";

// Custom styles for PlaceholderCard
import styles from "examples/Cards/PlaceholderCard/styles";

function PlaceholderCard({ icon, title, hasBorder, outlined }) {
  const classes = styles({ hasBorder });

  return (
    <Card
      raised
      className={clsx(classes.placeholderCard, {
        [classes.placeholderCard_outlined]: outlined,
      })}
    >
      <SuiBox
        display="flex"
        flexDirection="column"
        justifyContent="center"
        textAlign="center"
        height="100%"
        p={3}
      >
        <SuiBox color="secondary" mb={0.5}>
          <Icon fontSize="medium" className="font-bold">
            {icon}
          </Icon>
        </SuiBox>
        <SuiTypography variant={title.variant} textColor="secondary">
          {title.text}
        </SuiTypography>
      </SuiBox>
    </Card>
  );
}

// Setting default values for the props of PlaceholderCard
PlaceholderCard.defaultProps = {
  icon: "add",
  hasBorder: false,
  outlined: false,
};

// Typechecking props for the PlaceholderCard
PlaceholderCard.propTypes = {
  icon: PropTypes.node,
  title: PropTypes.shape({
    variant: PropTypes.string.isRequired,
    text: PropTypes.string.isRequired,
  }).isRequired,
  hasBorder: PropTypes.bool,
  outlined: PropTypes.bool,
};

export default PlaceholderCard;

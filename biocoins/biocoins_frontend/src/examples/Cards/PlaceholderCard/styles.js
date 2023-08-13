// @mui material components
import { makeStyles } from "@mui/styles";

export default makeStyles(({ palette, borders }) => {
  const { grey, transparent } = palette;
  const { borderWidth } = borders;

  return {
    placeholderCard: {
      height: "100%",
      border: ({ hasBorder }) => (hasBorder ? `${borderWidth[1]} solid ${grey[300]}` : "none"),
    },

    placeholderCard_outlined: {
      backgroundColor: transparent.main,
      border: `${borderWidth[1]} solid ${grey[300]} !important`,
      boxShadow: "none",
    },
  };
});

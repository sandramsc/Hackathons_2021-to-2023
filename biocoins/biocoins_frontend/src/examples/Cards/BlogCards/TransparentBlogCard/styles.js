// @mui material components
import { makeStyles } from "@mui/styles";

export default makeStyles(({ palette, boxShadows, functions, transitions }) => {
  const { transparent } = palette;
  const { regular } = boxShadows;
  const { pxToRem } = functions;

  return {
    card: {
      backgroundColor: transparent.main,
      boxShadow: "none",
      overflow: "visible",
    },

    card_image: {
      width: "100%",
      height: "auto",
      minHeight: pxToRem(235),
      margin: 0,
      boxShadow: regular,
      transformOrigin: "50% 0",
      transform: `perspective(${pxToRem(999)}) rotateX(0deg) translateZ(0)`,
      WebkitBackfaceVisibility: "hidden",
      backfaceVisibility: "hidden",
      willChange: "transform, box-shadow",
      transition: transitions.create("transform", {
        easing: transitions.easing.easeIn,
        duration: transitions.duration.shorter,
      }),

      "&:hover": {
        transform: `perspective(${pxToRem(999)}) rotateX(7deg) translate3d(0, ${pxToRem(
          -4
        )}, ${pxToRem(5)})`,
      },
    },

    card_action: {
      display: "inline-block",
      textDecoration: "none",

      "& .MuiTypography-root": {
        display: "flex",
        alignItems: "center",
      },

      "& .material-icons": {
        fontSize: "1.125rem",
        transform: `translateX(${pxToRem(2)})`,
        transition: "transform 0.2s cubic-bezier(0.34,1.61,0.7,1.3)",
      },

      "&:hover .material-icons, &:focus .material-icons": {
        transform: `translateX(${pxToRem(6)})`,
      },
    },
  };
});
